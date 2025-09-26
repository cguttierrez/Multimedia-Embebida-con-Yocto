#!/usr/bin/env python3
import gi
import cv2
import numpy as np

gi.require_version('Gst', '1.0')
from gi.repository import Gst

Gst.init(None)

# ====== Configuración ======
FILE_PATH = "/usr/share/video1.mp4"  # Ruta del video
BLOCK_SIZE = 100                     # Número de frames por bloque
OUTPUT_FILE = "rostros_totales.txt"
MIN_FACE_SIZE = 50
MIN_EYE_SIZE = 1                      # Tamaño mínimo de los ojos (ancho y alto)
MAX_PEOPLE_LIMIT = 5                  # Límite de personas para alerta
# ==========================

# Inicializar detectores Haar
face_cascade = cv2.CascadeClassifier("/usr/share/haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("/usr/share/haarcascade_eye.xml")

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

        frame = np.ndarray((height, width, 3), dtype=np.uint8, buffer=map_info.data).copy()
        buf.unmap(map_info)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(
            gray, scaleFactor=1.1, minNeighbors=5, minSize=(MIN_FACE_SIZE, MIN_FACE_SIZE)
        )

        # ==== Contador de rostros en este frame ====
        count_faces_in_frame = 0

        for (x, y, w, h) in faces:
            roi_gray = gray[y:y+h, x:x+w]
            eyes = eye_cascade.detectMultiScale(
                roi_gray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(MIN_EYE_SIZE, MIN_EYE_SIZE)
            )

            if len(eyes) >= 2:   # valida que efectivamente es un rostro
                total_faces += 1
                count_faces_in_frame += 1

        # ==== Verificación de alerta ====
        if count_faces_in_frame > MAX_PEOPLE_LIMIT:
            print("Alerta!!! El número de personas supera el límite permitido de",MAX_PEOPLE_LIMIT)
            print("Se detectaron:", count_faces_in_frame, "personas en el frame", frame_idx)

        faces_per_frame.append(count_faces_in_frame)

        frame_idx += 1
        block_count += 1

    if block_count == 0:
        break

# ====== Guardar resultados ======
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write("=== RESULTADOS FINALES ===\n\n")
    for i, num in enumerate(faces_per_frame, start=1):
        f.write(f"Frame {i}: {num} rostros\n")

print(f"Resultados de las cantidades de rostros están guardados en: {OUTPUT_FILE}")

pipeline.set_state(Gst.State.NULL)

