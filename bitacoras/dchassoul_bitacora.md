# [bitacora personal-Daniel Chassoul]
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Date 22-8-2025[Timezone]

### Summary of Activity
- Asignación inicial grupal

### Details/Observations
Se realiza una reunión inicial donde se propone que todos los integrantes estudien el flujo de trabajo de Yocto, Gstreamer y OpenCV

### Errores y soluciones
- 

### References/Links
- El documento guía del proyecto                                                                 
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Date 26-8-2025  [Timezone]

### Summary of Activity
- Estudio del flujo de Gstreamer

### Details/Observations

- Se estudia el pipeline de Gstreamer con el fin de familiarizarse mejor con la aplicación para el desarrollo del proyecto

### Errores y soluciones


### References/Links
- ### GStreamer workshop.PDF visto en clase
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Date 30-8-2025  [Timezone]

### Summary of Activity
- El grupo llega al acuerdo de seleccionar la aplicación de reconocimiento de rostros como la aplicación que será incluída y desarrollada para la imagen mínima del proyecto

### Details/Observations
- Se hicieron algunas pruebas a la aplicación y se verifica que la aplicación realice la integración de gstremer y opencv mediante python
### Errores y soluciones

### References/Links
- 

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Date 2-9-2025  [Timezone]

### Summary of Activity

- Pruebas iniciales del script de python desarrollado en la computadora local

### Details/Observations

- Una vez realizado el código inicial de python para la aplicación de reconocer rostros se procede a realizar pruebas con el fin de observar si el código funciona en la computadora host y si el funcionamiento de la aplicación es el esperado. 

### Errores y soluciones

### References/Links

- 

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Date 3-9-2025  [Timezone]

### Summary of Activity
- Discución sobre el flujo de trabajo de Yocto

### Details/Observations
- Se analiza y discute el flujo de trabajo para todos los integrantes con el fin de lograr integrarlo al proyecto


### Errores y soluciones



### References/Links
- https://docs.yoctoproject.org/4.0.4/ref-manual/images.html
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Date 4-9-2025  [Timezone]

### Summary of Activity
- Compilación de la imagen mínima para correrla en virtual box

### Details/Observations
- Se compiló la imagen mínima de manera normal con el fin de intentar correrla en el entorno de virtual box, sin embargo, se generó un .iso mediante la configuración del local.conf el cual permitía la creación de la máquina virtual pero al momento de intentar correrla daba error y no se pudo concretar la imagen en el entorno de virtual box.

### Errores y soluciones
- Error crítico al intentar correr la imagen mínima en virtual box. 

### References/Links

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Date 6-9-2025  [Timezone]

### Summary of Activity
- Ejecución adecuada de la imagen en virtual box

### Details/Observations
- Gracias a la aporte de un integrante del grupo se logró generar una imagen capaz de ser corrida en virtual box, esto mediante la generación de un archivo vmdk en el local.conf utilizando #Image Format
IMAGE_FSTYPES += "wic.vmdk wic iso"

### Errores y soluciones
- Error: Anteriormente no se lograba cargar la imagen mínima al utilizar un .iso
- Solución: Se genera una imagen .wic.vmdk, la cual si es cargada desde disco duro de la virtual box

### References/Links
- https://docs.oracle.com/en/virtualization/virtualbox/6.0/user/vdidetails.html
- https://docs.yoctoproject.org/3.2.4/dev-manual/dev-manual-qemu.html
- 
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Date 8-9-2025  [Timezone]

### Summary of Activity
- Incorporación de gstreamer, opencv y python3 a la imagen mínima

### Details/Observations
- Se encuentra un repositorio en Internet que incluye las capas para incorporar Gstreamer, OpenCV y python3 a la imagen mínima de Yocto. Se clonó el repositorio el cual corresponde a la capa llamada meta-openembedded, de donde se escogieron manualmente las capas meta-oe, meta-multimedia y meta-python en el bblayers ya que estas 3 capas incorporan las recetas correspondientes para incluir opencv, python3 y gstreamer. La primera vez que se compiló la imagen no funcionó la compilación ya que no se tuvieron en cuenta las dependencias. 
Se realizó el cambio incluyendo las dependencias en el local.conf y al volver a compilar no dio errores y se verificó que sí se incluyó python, opencv y gstreamer a la imagen.

### Errores y soluciones
- Error: No incluir las dependencias necesarias para las aplicaciones a instalar
- Solución: Incluir las dependencias necesarias en el archivo local.conf para evitar problemas en la compilación de la imagen
### References/Links
- https://github.com/openembedded/meta-openembedded 
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Date 9-9-2025  [Timezone]

### Summary of Activity
- Desarrollo inicial de la receta para la aplicación de python 

### Details/Observations
- Se inicia con el desarrollo de la receta para incorporar el script de python realizado para reconocer rostros en la imagen mínima. Para esto, se estudia la estructura de una receta estándar de Yocto. Para esto se crea e incorpora la capa meta-custom, sin embargo, a la hora de incluir la receta e intentar realizarle el bitbake se encontraron con varios problemas. El primero fue el uso de comandos en la receta que solo eran aceptados por versiones anteriores de poky por lo cual saltaba error a la hora de la compilación. El segundo fue no incluir el CORE_IMAGE_EXTRA_INSTALL correspondiente a la receta del script de python. 


### Errores y soluciones
- Errores: Uso incorrecto de la estructura de las recetas y falta de inclusión de CORE_IMAGE_EXTRA_INSTALL en el local.conf
- Soluciones: Cambiar los comandos de la receta de Yocto a comandos soportados por la versiones recientes, además se agregó en el local.conf la siguiente línea CORE_IMAGE_EXTRA_INSTALL += "reconoce-rostros"


### References/Links
- 
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Date 9-9-2025  [Timezone]

### Summary of Activity
-  Intento de correr el script de python en la máquina virtual 

### Details/Observations
- Una vez se logró incorporar el script realizado para la aplicación se probó a correrlo dentro de la imagen, sin embargo, al intentar correrlo saltaba el siguiente error: "ModuleNotFoundError: No module named 'gi'". Al investigar en Internet se descubrió que para ese módulo en específico incluído en el código es necesario incluir la dependecia     gstreamer1.0-libav. Una vez incorporado esto se solucionó el error, pero nuevamente saltó un nuevo error ya que el código hace uso de un archivo llamado haarscade.xml el cual no había sido incluído en ninguna receta hasta este punto. 


### Errores y soluciones
- Error: El error al no incluir una dependencia necesaria de gstreamer para el correcto funcionamiento de la aplicación, además de no incluir el archivo .xml utilizado en el script.
- Solución: En esta sesión solo solucionó el problema correspondiente con la dependencia de gstreamer, incluyendóla en local.conf mediante la línea gstreamer1.0-libav. 

### References/Links
- 
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Date 10-9-2025  [Timezone]

### Summary of Activity
- Inclusión de la receta para incorporar el archivo haarcades.xml 

### Details/Observations
- Se realizó la receta correspondiente para incluir el archivo haarscades.xml en la imagen mínima. El archivo fue obtenido de un repositorio en GitHub. 

### Errores y soluciones
- Se logra dar solución al error pendiente de la actualización anterior.

### References/Links
- https://github.com/opencv/opencv/tree/master/data/haarcascades
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
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Date 21-9-2025  [Timezone]

### Summary of Activity

-  Correr el proyecto completo 

### Details/Observations

- Una vez solucionados todos los problemas anteriores, el grupo procede a correr la imagen mínima completa en virtual box y se verifica el correcto funcionamiento de todas las componentes necesarias para el desarrollo de la aplicación

### Errores y soluciones

- No aplica

### References/Links

- 

## Date 23-9-2025  [Timezone]

### Summary of Activity

-  Creación del documento tutorial 

### Details/Observations

- El grupo procede a la realización del documento tutorial, detallando cada uno de los aspectos realizados en el proyecto y cómo se realizaron

### Errores y soluciones

- No aplica

### References/Links

- 
