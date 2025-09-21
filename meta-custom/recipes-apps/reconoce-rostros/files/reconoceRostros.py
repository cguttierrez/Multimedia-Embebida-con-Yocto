#!/usr/bin/env python3
import gi
import cv2
import numpy as np

gi.require_version('Gst', '1.0')
from gi.repository import Gst

Gst.init(None)

# ====== Configuración ======
FILE_PATH = "/usr/share/video2.mp4"  # Ruta del video
BLOCK_SIZE = 100                     # Número de frames por bloque
OUTPUT_FILE = "rostros_totales.txt"
MIN_FACE_SIZE = 100
# ==========================

# Inicializar detector Haar
face_cascade = cv2.CascadeClassifier("/usr/share/haarcascade_frontalface_default.xml") 

# Pipeline GStreamer → OpenCV
pipeline_str = (
    f"filesrc location={FILE_PATH} ! decodebin ! videoconvert ! "
    "video/x-raw,format=BGR ! appsink name=sink emit-signals=true"
)
pipeline = Gst.parse_launch(pipeline_str)
appsink = pipeline.get_by_name("sink")

# Evitar acumulamiento de buffers
appsink.set_property("max-buffers", 1)
appsink.set_property("drop", True)

pipeline.set_state(Gst.State.PLAYING)

frame_idx = 0
total_faces = 0
faces_per_frame = []

while True:
    block_count = 0
    # Procesar un bloque de frames
    while block_count < BLOCK_SIZE:
        sample = appsink.emit("try-pull-sample", Gst.SECOND)
        if not sample:
            break  # fin de video

        buf = sample.get_buffer()
        caps = sample.get_caps().get_structure(0)
        width, height = caps.get_value("width"), caps.get_value("height")

        success, map_info = buf.map(Gst.MapFlags.READ)
        if not success:
            continue

        # Convertir buffer a frame (sin .copy() para ahorrar RAM)
        frame = np.ndarray((height, width, 3), dtype=np.uint8, buffer=map_info.data)
        buf.unmap(map_info)

        # Detección de rostros
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(
            gray, scaleFactor=1.1, minNeighbors=5, minSize=(MIN_FACE_SIZE, MIN_FACE_SIZE)
        )
        count_faces = len(faces)
        if count_faces > 10:
            print("Alerta!!! el número de personas supera el límite")
            print("Se detectaron:", count_faces, "personas") 
        total_faces += count_faces
        faces_per_frame.append(count_faces)

        frame_idx += 1
        block_count += 1

    if block_count == 0:
        break  # no quedaron más frames

# Guardar resultados
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write("=== RESULTADOS FINALES ===\n\n")
    for i, num in enumerate(faces_per_frame, start=1):
        f.write(f"Frame {i}: {num} rostros\n")
    f.write("\n")
  

print(f"Resultados guardados en: {OUTPUT_FILE}")

pipeline.set_state(Gst.State.NULL)
