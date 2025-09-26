# [bitacora personal-Carlos Gutierrez]
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
- Generacion de imagenes booteables para la virtual box en el local.conf con #Image Format
IMAGE_FSTYPES += "wic.vmdk wic iso"

### Errores y soluciones
- Error: La imagen iso creada no funciona ya que la virtual box no la carga
- Solucion: Se genera una imagen .wic.vmdk, la cual si es cargada desde disco duro de la virtual box

### References/Links
- https://docs.oracle.com/en/virtualization/virtualbox/6.0/user/vdidetails.html
- https://docs.yoctoproject.org/3.2.4/dev-manual/dev-manual-qemu.html
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
- Solucion volver a instalar yocto project, con los nuevos paquetes, ya que anteriormente se habian corrompido algunos archivos
- Adem'as de agregar la capa meta-openembedded junto a paquetes de python, opencv y gstreamer, y V4L2
### References/Links
- https://github.com/openembedded/meta-openembedded 
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Date 11-9-2025  [Timezone]

### Summary of Activity
- Compilación de la imagen sato y minima, con la aplicaci'on de reconocimiento de video en tiempo real 

### Details/Observations
- Se agrego una capa para agregar el programa de python en la imagen


### Errores y soluciones
- Errores a la hora de ver el dispositivo de la camara web en la imagen, v4l2 no reconoce la camara por lo que el programa no funciona correctamente
- Se incluye el dispositivo desde la virtual box, sin embargo sigue sin funcionar
- el archivo de python se debe establecer de tipo 0755 para establecerlo como ejecutable

### References/Links
- 
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Date 13-9-2025  [Timezone]

### Summary of Activity
-  reconocimiento de la webcam 

### Details/Observations
- Tratar de que la webcam sea reconocida por la maquina virtual ya que anteriormente tenemos problemas para que el v4l2 lo reconozca


### Errores y soluciones
- La Virtual box reconoce la camara en super usuario sin embargo, la imagen de yocto no parece poder hacerlo

### References/Links
- 
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Date 16-9-2025  [Timezone]

### Summary of Activity
-  Consulta con el profesor
-  Imagen no puede reconocer la camara 

### Details/Observations
- Mediante la aclaracion del profesor de que la imagen de yocto no puede reconocer las camaras, procedemos a usar un video como archivo a ser procesado por la aplicacion y cuyo resultado final seria los datos obtenido de los rostros por frame en un archivo .txt
- Se procedio a cambiar el programa para que en lugar de usar video directamente de la webcam lo usara proveniente a un archivo .mp4 

### Errores y soluciones
- Se logra crear un programa necesario para que no use video de la webcam

### References/Links
- 
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Date 18-9-2025  [Timezone]

### Summary of Activity
-  Recrear la imagen con el nuevo programa

### Details/Observations
- Se recrea la imagen con las nuevas caracteristicas del programa para sintetizar la aplicacion en la virtual box
### Errores y soluciones
- La biblioteca de opencv no detecta el haarcascade dentro de la imagen por lo que el programa no funciona
- Se sube la imagen con el archivo haarcascade.xml en diferente receta para poder ser instalada en la imagen junto con el programa, sin embargo no lo reconoce

### References/Links
- 
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Date 20-9-2025  [Timezone]

### Summary of Activity
-  Reconocimiento de haarcascade por el programa de python

### Details/Observations
- haarcascade necesita ser reconocido por el programa de python para el reconocimiento, sospecho que hay errores en la direcciones
- Se logra correr el programa al reconocer el haarcascade.xml
- Adem'as se agrega el video en otra receta aparte dentro de la misma capa personalizada
- Se identifica el archivo de texto y se logra leer con el comando less
### Errores y soluciones
- Se logra que el programa reconozca el archivo .xml estableciendo la direcci'on datadir que se direcciona a la carpeta /usr/share de la imagen
- Es necesario establecer el archivo como 0644 para indicar que es un archivo de lectura

### References/Links
- https://superuser-com.translate.goog/questions/1511606/are-these-the-correct-permissions-644-and-755-for-files-and-directories-on-a-w?_x_tr_sl=en&_x_tr_tl=es&_x_tr_hl=es&_x_tr_pto=tc
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Date 21-9-2025 22-9-2025 23-9-2025 [Timezone]

### Summary of Activity
-  Intento de mejorar el reconocimiento de rostros y seleccion de mejores videos

### Details/Observations
- La aplicacion reconoce rostros donde no los hay por lo que hay picos falsos de numero de rostros en algunos frames
### Errores y soluciones
- Se agreg'o la condicion de que reconociera rostros solo si hay ojos, esto mejora el contador de rostros reales
- No reconoce rostros con ojos muy pequenos o si usan lentes
- Precision de los modelos entrenados probocan fallas en la precisi'on de la aplicacion

### References/Links

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Date 21-9-2025 22-9-2025 23-9-2025 [Timezone]

### Summary of Activity
-  Correción de machine al generar imagen 

### Details/Observations
- La imagen se debe generar genericx86-64, ya que se estaba genrando con la qemux86-64 
### Errores y soluciones
- La imagen no se carga correctamente en la virtualbox
- Se soluciona marcando la casilla UEFI debido a que la machine genericx86-64 requiere de una UEFI  para cargar la imagen


### References/Links
Consulta
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

