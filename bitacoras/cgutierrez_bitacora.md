# 26-8-2025 - [bitacora personal-Carlos Gutierrez]
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Date 24-8-2025[Timezone]

### Summary of Activity
- Investigacion sobre el flujo con el marco de trabajo de Gstreamer

### Details/Observations
Se investigó sobre los paquetes necesarios para GStreamer, tales como:
    gst-libav : complemento basado en Libav que contiene muchos decodificadores y codificadores.
    gst-plugins-bad : complementos que necesitan más calidad, pruebas o documentación.
    gst-plugins-base : conjunto ejemplar esencial de elementos.
    gst-plugins-good - Complementos de buena calidad bajo licencia LGPL.
    gst-plugins-ugly : complementos de buena calidad que podrían plantear problemas de distribución.


### Errores y soluciones
- 

### References/Links
- Lo visto en clase para GSTreamer                                                                     
- https://wiki-archlinux-org.translate.goog/title/GStreamer?_x_tr_sl=en&_x_tr_tl=es&_x_tr_hl=es&_x_tr_pto=tc
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Date 26-8-2025  [Timezone]

### Summary of Activity
- Aplicación: Reconocimiento de rostros y contador 

### Details/Observations
Se desarrollará una aplicación que tome el video de la webcam con el siguiente pipeline:
pipeline_str = ("v4l2src device=/dev/video0 ! videoconvert ! video/x-raw,format=BGR ! appsink name=sink emit-signals=true") 

v4l2src device=/dev/video0 → usa la webcam principal (normalmente /dev/video0).

videoconvert → convierte al formato de video crudo.

video/x-raw,format=BGR → especifica el formato para que OpenCV lo entienda.

appsink → permite recibir los frames en tu código Python con OpenCV.

### Errores y soluciones


### References/Links
- https://stackoverflow.com/questions/63920639/conversion-of-gstreamer-launch-to-opencv-pipeline-for-camera-ov9281
- https://github.com/futurelabmx/FaceRecognition2
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Date 30-8-2025  [Timezone]

### Summary of Activity
- Selección de la aplicación en el forms y la conformación de dicha aplicación en grupos
- ...

### Details/Observations
Se hicieron algunas pruebas a la aplicación y se hizo la consulta a los compañeros para elegir dicha aplicación

### Errores y soluciones

### References/Links
- 

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Date 31-8-2025  [Timezone]

### Summary of Activity
- [Key action 1]
- [Key action 2]
- ...

### Details/Observations
[Detailed description of what was done, challenges encountered, solutions implemented, and any relevant observations. Include code snippets or command outputs if helpful.]

### Decisions Made
- [Decision 1 and its rationale]
- [Decision 2 and its rationale]

### Next Steps/To-Do
- [Action item 1]
- [Action item 2]

### References/Links
- [Link to relevant issue, pull request, or external resource]

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
