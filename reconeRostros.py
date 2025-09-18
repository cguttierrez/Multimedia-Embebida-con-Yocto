#!/usr/bin/env python3
import gi
import cv2
import numpy as np
import sys
import time
import pickle
import os
from collections import defaultdict

gi.require_version('Gst', '1.0')
from gi.repository import Gst
Gst.init(None)

# ====== Configuración ======
FILE_PATH = "video_prueba_1.mp4"   # <-- Cambia esto por tu archivo
SIMILARITY_THRESHOLD = 0.85  # Umbral de similitud para considerar rostros iguales
MIN_FACE_SIZE = 50  # Tamaño mínimo de rostro para procesar
FACE_DATA_FILE = "unique_faces.pkl"

class SimpleFaceTracker:
    def __init__(self, similarity_threshold=0.85):
        self.known_faces = []  # Lista de rostros conocidos (histogramas)
        self.known_face_ids = []
        self.person_count = 0
        self.similarity_threshold = similarity_threshold
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        
    def extract_face_features(self, face_roi):
        """Extraer características del rostro usando histograma"""
        # Convertir a escala de grises y redimensionar
        gray_face = cv2.cvtColor(face_roi, cv2.COLOR_BGR2GRAY)
        resized_face = cv2.resize(gray_face, (100, 100))
        
        # Ecualizar histograma para mejor comparación
        equalized = cv2.equalizeHist(resized_face)
        
        # Calcular histograma LBP (Local Binary Pattern) simplificado
        lbp_hist = self.calculate_simple_lbp_histogram(equalized)
        
        return lbp_hist
    
    def calculate_simple_lbp_histogram(self, image):
        """Calcular un histograma LBP simplificado"""
        height, width = image.shape
        lbp = np.zeros((height-2, width-2), dtype=np.uint8)
        
        # Calcular LBP básico
        for i in range(1, height-1):
            for j in range(1, width-1):
                center = image[i, j]
                code = 0
                
                # 8 vecinos
                neighbors = [
                    image[i-1, j-1], image[i-1, j], image[i-1, j+1],
                    image[i, j+1], image[i+1, j+1], image[i+1, j],
                    image[i+1, j-1], image[i, j-1]
                ]
                
                for k, neighbor in enumerate(neighbors):
                    if neighbor >= center:
                        code += 2**k
                
                lbp[i-1, j-1] = code
        
        # Calcular histograma
        hist = cv2.calcHist([lbp], [0], None, [256], [0, 256])
        hist = cv2.normalize(hist, hist).flatten()
        
        return hist
    
    def compare_faces(self, face_features1, face_features2):
        """Comparar dos conjuntos de características faciales"""
        # Usar correlación como medida de similitud
        correlation = cv2.compareHist(face_features1, face_features2, cv2.HISTCMP_CORREL)
        return correlation
    
    def find_matching_person(self, face_features):
        """Buscar si el rostro coincide con alguna persona conocida"""
        best_match_score = 0
        best_match_idx = -1
        
        for idx, known_face in enumerate(self.known_faces):
            similarity = self.compare_faces(face_features, known_face)
            
            if similarity > best_match_score:
                best_match_score = similarity
                best_match_idx = idx
        
        if best_match_score >= self.similarity_threshold:
            return self.known_face_ids[best_match_idx], best_match_score
        
        return None, best_match_score
    
    def add_new_person(self, face_features):
        """Agregar una nueva persona"""
        self.person_count += 1
        person_id = f"Persona_{self.person_count}"
        self.known_faces.append(face_features)
        self.known_face_ids.append(person_id)
        return person_id
    
    def process_frame(self, frame):
        """Procesar frame y detectar personas únicas"""
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(
            gray, 
            scaleFactor=1.1, 
            minNeighbors=5,
            minSize=(MIN_FACE_SIZE, MIN_FACE_SIZE)
        )
        
        current_frame_persons = []
        processed_faces = []
        
        for (x, y, w, h) in faces:
            # Extraer ROI del rostro
            face_roi = frame[y:y+h, x:x+w]
            
            if face_roi.size == 0:
                continue
                
            try:
                # Extraer características
                face_features = self.extract_face_features(face_roi)
                
                # Buscar coincidencia
                person_id, similarity = self.find_matching_person(face_features)
                
                if person_id is None:
                    # Nueva persona
                    person_id = self.add_new_person(face_features)
                    print(f"Nueva persona detectada: {person_id}")
                    color = (0, 255, 0)  # Verde para nueva persona
                else:
                    color = (255, 0, 0)  # Azul para persona conocida
                
                current_frame_persons.append(person_id)
                processed_faces.append({
                    'id': person_id,
                    'bbox': (x, y, w, h),
                    'similarity': similarity,
                    'color': color
                })
                
            except Exception as e:
                print(f"Error procesando rostro: {e}")
                continue
        
        # Dibujar resultados
        for face_info in processed_faces:
            x, y, w, h = face_info['bbox']
            person_id = face_info['id']
            similarity = face_info['similarity']
            color = face_info['color']
            
            # Rectángulo
            cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)
            
            # Fondo para texto
            cv2.rectangle(frame, (x, y-40), (x+w, y), color, cv2.FILLED)
            
            # Texto con ID y similitud
            text = f"{person_id} ({similarity:.2f})"
            cv2.putText(frame, text, (x+2, y-10), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
        
        return frame, current_frame_persons
    
    def save_data(self, filepath):
        """Guardar datos de rostros"""
        data = {
            'faces': self.known_faces,
            'ids': self.known_face_ids,
            'count': self.person_count
        }
        try:
            with open(filepath, 'wb') as f:
                pickle.dump(data, f)
        except Exception as e:
            print(f"Error guardando datos: {e}")
    
    def load_data(self, filepath):
        """Cargar datos de rostros"""
        if os.path.exists(filepath):
            try:
                with open(filepath, 'rb') as f:
                    data = pickle.load(f)
                self.known_faces = data['faces']
                self.known_face_ids = data['ids']
                self.person_count = data['count']
                print(f"Cargados {self.person_count} rostros conocidos")
            except Exception as e:
                print(f"Error cargando datos: {e}")

def make_wait_frame(width, height):
    img = np.zeros((height, width, 3), dtype=np.uint8)
    cv2.putText(img, "Esperando frames...", (30, height//2),
                cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255,255,255), 2)
    return img

# ====== Pipeline GStreamer ======
pipeline_str = (
    f"filesrc location={FILE_PATH} ! decodebin ! videoconvert ! "
    "video/x-raw,format=BGR ! appsink name=sink emit-signals=true"
)

try:
    # Inicializar tracker
    tracker = SimpleFaceTracker(similarity_threshold=SIMILARITY_THRESHOLD)
    
    # Cargar datos previos si existen
    tracker.load_data(FACE_DATA_FILE)
    
    pipeline = Gst.parse_launch(pipeline_str)
    appsink = pipeline.get_by_name("sink")
    pipeline.set_state(Gst.State.PLAYING)
    
    print("=== DETECTOR DE PERSONAS ÚNICAS (OpenCV) ===")
    print(f"Archivo: {FILE_PATH}")
    print(f"Umbral de similitud: {SIMILARITY_THRESHOLD}")
    print(f"Tamaño mínimo de rostro: {MIN_FACE_SIZE}px")
    print("Presiona 'q' para cerrar.")
    print("=" * 50)
    
    cv2.namedWindow("Detección de Personas Únicas", cv2.WINDOW_NORMAL)
    
    last_sample_time = time.time()
    width, height = 640, 480
    wait_frame = make_wait_frame(width, height)
    frame_count = 0
    
    # Archivo de salida
    with open("personas_unicas_opencv.txt", "w") as output_file:
        output_file.write("=== DETECCIÓN DE PERSONAS ÚNICAS (OpenCV) ===\n")
        output_file.write(f"Umbral de similitud: {SIMILARITY_THRESHOLD}\n")
        output_file.write(f"Tamaño mínimo de rostro: {MIN_FACE_SIZE}px\n")
        output_file.write("=" * 50 + "\n\n")
        
        while True:
            sample = appsink.emit("try-pull-sample", Gst.SECOND)
            
            if not sample:
                if time.time() - last_sample_time > 2:
                    cv2.imshow("Detección de Personas Únicas", wait_frame)
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break
                continue
            
            # Extraer frame
            buf = sample.get_buffer()
            caps = sample.get_caps().get_structure(0)
            width = caps.get_value("width")
            height = caps.get_value("height")
            
            success, map_info = buf.map(Gst.MapFlags.READ)
            if not success:
                continue
                
            frame = np.ndarray(
                (height, width, 3),
                dtype=np.uint8,
                buffer=map_info.data
            ).copy()
            buf.unmap(map_info)
            
            last_sample_time = time.time()
            frame_count += 1
            
            # Procesar frame
            processed_frame, current_persons = tracker.process_frame(frame)
            
            # Información en pantalla
            info_texts = [
                f"Frame: {frame_count}",
                f"Personas únicas: {tracker.person_count}",
                f"Rostros en frame: {len(current_persons)}",
                f"Umbral: {SIMILARITY_THRESHOLD}"
            ]
            
            y_pos = 30
            for text in info_texts:
                cv2.putText(processed_frame, text, (10, y_pos),
                           cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)
                y_pos += 25
            
            cv2.imshow("Detección de Personas Únicas", processed_frame)
            
            # Guardar información
            if len(current_persons) > 0:
                output_file.write(f"Frame {frame_count}:\n")
                output_file.write(f"  Rostros detectados: {len(current_persons)}\n")
                output_file.write(f"  Personas: {', '.join(set(current_persons))}\n")
                output_file.write(f"  Total personas únicas: {tracker.person_count}\n\n")
                output_file.flush()
            
            # Salir con 'q'
            if cv2.waitKey(1) & 0xFF == ord('q'):
                print("\nCerrando...")
                break
        
        # Resumen final
        print(f"\n=== RESULTADOS FINALES ===")
        print(f"Total de personas únicas: {tracker.person_count}")
        print(f"IDs: {tracker.known_face_ids}")
        
        output_file.write("\n=== RESUMEN FINAL ===\n")
        output_file.write(f"Total de personas únicas detectadas: {tracker.person_count}\n")
        output_file.write(f"Lista de personas: {', '.join(tracker.known_face_ids)}\n")
    
    # Guardar datos para próxima ejecución
    tracker.save_data(FACE_DATA_FILE)
    print(f"Datos guardados en: {FACE_DATA_FILE}")
    
    # Limpiar
    pipeline.set_state(Gst.State.NULL)
    cv2.destroyAllWindows()
    
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
