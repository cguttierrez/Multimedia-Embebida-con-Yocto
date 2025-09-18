#!/usr/bin/env python3
import gi
import cv2
import numpy as np
from gi.repository import Gst

gi.require_version('Gst', '1.0')
Gst.init(None)

# ====== Configuración ======
FILE_PATH = "video2.mp4"           # Ruta del video
MAX_FRAMES = 100000                   # Número máximo de frames a procesar
OUTPUT_FILE = "rostros_totales.txt"  # Archivo de salida
MIN_FACE_SIZE = 100                 # Tamaño mínimo de rostro
# ==========================

# Inicializar detector Haar
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# Pipeline GStreamer → OpenCV
pipeline_str = (
    f"filesrc location={FILE_PATH} ! decodebin ! videoconvert ! "
    "video/x-raw,format=BGR ! appsink name=sink emit-signals=true"
)
pipeline = Gst.parse_launch(pipeline_str)
appsink = pipeline.get_by_name("sink")
pipeline.set_state(Gst.State.PLAYING)

frame_idx = 0
total_faces = 0

# Lista para almacenar rostros por frame
faces_per_frame = []

while True:
    if frame_idx >= MAX_FRAMES:
        break

    sample = appsink.emit("try-pull-sample", Gst.SECOND)
    if not sample:
        break

    buf = sample.get_buffer()
    caps = sample.get_caps().get_structure(0)
    width, height = caps.get_value("width"), caps.get_value("height")

    success, map_info = buf.map(Gst.MapFlags.READ)
    if not success:
        continue

    frame = np.ndarray(
        (height, width, 3),
        dtype=np.uint8,
        buffer=map_info.data
    ).copy()
    buf.unmap(map_info)

    frame_idx += 1

    # Detección de rostros
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(
        gray, scaleFactor=1.1, minNeighbors=5, minSize=(MIN_FACE_SIZE, MIN_FACE_SIZE)
    )
    count_faces = len(faces)
    total_faces += count_faces
    faces_per_frame.append(count_faces)  # Guardar cantidad por frame

# Guardar resultados en .txt
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write("=== RESULTADOS FINALES ===\n\n")
    for i, num in enumerate(faces_per_frame, start=1):
        f.write(f"Frame {i}: {num} rostros\n")
    f.write("\n")
    f.write(f"Frames procesados: {frame_idx}\n")
    f.write(f"Total de rostros detectados: {total_faces}\n")

print(f"Resultados guardados en: {OUTPUT_FILE}")
print(f"Frames procesados: {frame_idx}")
print(f"Total de rostros detectados: {total_faces}")

pipeline.set_state(Gst.State.NULL)
