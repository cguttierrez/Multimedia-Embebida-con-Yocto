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
- Selección de la aplicación para el forms y la conformación de dicha aplicación en grupos
- ...

### Details/Observations
- Se hicieron algunas pruebas a la aplicación y se hizo la consulta a los compañeros para elegir dicha aplicación
- Se organizaron dos reuniones una para el miércoles y otra para el fin de semana
### Errores y soluciones

### References/Links
- 

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Date 3-9-2025  [Timezone]

### Summary of Activity
- Discución sobre el flujo de trabajo en yocto para con la integración de la aplicación
- ...

### Details/Observations
- Se discutió sobre los requisitos que debía tener la aplicación en la imagen, por lo que se optó usar la imagen de sato debido a la integración multimedia, esto debido a que la aplicación requería de uso de cámara, mostrar el video en tiempo real captado por la cámara, además de generar la imagen para la virtual box


### Errores y soluciones



### References/Links
- https://docs.yoctoproject.org/4.0.4/ref-manual/images.html
- 
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Date 4-9-2025  [Timezone]

### Summary of Activity
- Compilación de la imagen minima y sato en la virtual box

### Details/Observations
- Se trató de compilar la imagen mínima para la virtual box, por lo que, se trató de pasar la imagen creada por yocto a una imagen .iso para virtualbox
- Se le hizo la consula al chat bot Chat GPT de como podría realizar la tarea de generar un .iso, por lo que trató de crear un  booteable a partir de los archivos que genera Yocto, se preparó una carpeta con esos archivos .ext4 junto con un cargador de arranque isolinux y luego se usa mkisofs para empaquetar todo en un archivo .iso

### Errores y soluciones
- La generación del .iso no se concretó
- 

### References/Links
- [https://docs.yoctoproject.org/4.0.4/ref-manual/images.html](https://unix.stackexchange.com/questions/541405/how-can-i-create-an-image-of-a-partition-ext4-and-later-mount-it-to-browse-res)
- https://superuser.com/questions/1605786/how-can-i-make-an-ext4-iso-either-from-a-bootable-drive-or-from-iso9660
- https://askubuntu.com/questions/1107281/how-do-i-create-a-bootable-live-usb-that-uses-ext4-opposed-to-iso-9660-squashfs
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Date 6-9-2025  [Timezone]

### Summary of Activity
- Ejecución adecuada para generar la imagen .iso en yocto

### Details/Observations
- 

### Errores y soluciones
- 
- 

### References/Links
- 
- 
- 
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Date 8-9-2025  [Timezone]

### Summary of Activity
- Compilación de la imagen minima y sato en virtual box

### Details/Observations
- Se trató de compilar la imagen mínima añadiendo paquetes necesario para compilar la receta, siendo python3, GStreamer, opencv y v2l4


### Errores y soluciones
- Errores a la hora de compilar la imagen debido a alteraciones en el local.conf y creacciones de layer propias con recetas incorrectas
- Se eliminaron las recetas y se agregaron nuevas pero seguían surgiendo los errores a la hora del volver a compilar las tareas, saltaban errores de que no existian algunos paquetes pertenecientes a opencv.

### References/Links
- 
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Date 9-9-2025  [Timezone]

### Summary of Activity
- Compilación de la imagen minima y sato sato en virtual box

### Details/Observations
- Nuevamente se trata de compilar la imagen mínima añadiendo paquetes necesarios para darle soporte a la aplicación de python


### Errores y soluciones
- Errores a la hora de compilar la imagen debido a alteraciones en el local.conf y creacciones de layer propias con recetas incorrectas
- Se eliminaron las recetas y se agregaron nuevas pero seguían surgiendo los errores a la hora del volver a compilar las tareas, saltaban errores de que no existian algunos paquetes pertenecientes a opencv.

### References/Links
- 
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

