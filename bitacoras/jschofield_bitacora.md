# [bitacora personal- Jorge Schofield]
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Date 26-8-2025

### Summary of Activity
- Estudiar el flujo de trabajo de Yocto, GStreamer y OpenCV antes de iniciar con
el código o con la implementación en Yocto.

### Details/Observations
- El equipo hizo el "Hello World!" de Yocto.
  
### Errores y soluciones
- 

### References/Links
- https://wiki-archlinux-org.translate.goog/title/GStreamer?_x_tr_sl=en&_x_tr_tl=es&_x_tr_hl=es&_x_tr_pto=tc                                                                     
- https://docs.yoctoproject.org/dev/ref-manual/index.html
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Date 28-8-2025  

### Summary of Activity
- Se discutieron las ideas para la aplicación y lo aprendido de los flujos de trabajo. 

### Details/Observations
- Aplicación: tomar un video de una cámara y reconocer personas.
Se buscaron las bibliotecas necesarias para implementar en Python el código. 

### Errores y soluciones
-

### References/Links
- https://stackoverflow.com/questions/63920639/conversion-of-gstreamer-launch-to-opencv-pipeline-for-camera-ov9281
- https://github.com/futurelabmx/FaceRecognition2
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Date 30-8-2025  

### Summary of Activity
- Se escribió el primer código de prueba y se escribió la idea en el forms. 

### Details/Observations
- Se hicieron algunas pruebas para reconocer las dependencias del código.

### Errores y soluciones
-

### References/Links
- 

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Date 4-9-2025  

### Summary of Activity
- Primera integración en Yocto utilizando la imagen sato.

### Details/Observations
- Se decidió usar la imagen de sato por el uso de la cámara en tiempo de real.

### Errores y soluciones
- No se encontraban las dependencias de algunas recetas. 
- La imagen duraba mucho en correr y el tiempo de prueba era lento.

### References/Links
- https://docs.yoctoproject.org/4.0.4/ref-manual/images.html

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Date 10-9-2025  

### Summary of Activity
- Cambio de la aplicación y de imagen. 

### Details/Observations
- Ahora se utilizará una imagen mínima con solo lo requerido para contar los rostros de un video y mostrar en la consola una alerta si supera cierta cantidad.
- Después de la consulta se decidió hacer estos cambios. 
  
### Errores y soluciones
- No se podía cargar la imagen mínima utilizado el formato .iso.
  S/ Se buscó que el formato correcto debería ser .vmdk para correr esta imagen en VirtualBox.

### References/Links
- https://erickof.medium.com/yocto-project-tutorial-baking-a-minimal-linux-image-from-scratch-625b3e65f768

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Date 11/17-9-2025  

### Summary of Activity
- Desarrollo de la nueva aplicación y elaboración de videos de prueba. 

### Details/Observations
- Se validó su funcionalidad.

### Errores y soluciones
- Falta de bibliotecas necesarias para la nueva implementación.
  S/ Se buscaron las nuevas dependencias y se integraron tanto en las recetas como en el código de python.

### References/Links
- 
  
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Date 18-9-2025  

### Summary of Activity
- Se desarrolló una receta en Yocto que contenía todos los paquetes necesarios para la imagen mínima.  

### Details/Observations
- Se hizo la prueba y se validó en qemu que dentro de la máquina virtual existían los archivos necesarios (python3, gstreamer, opencv,...).

### Errores y soluciones
- No se encontraban todos los paquetes.
- Problemas de dependencias con la receta nueva.
- Desaparición del archivo deploy (no se creaba al hacer bitbake).
  S/ Se verificaron los archivos de local.conf y bblayers.conf para confirmar que estaban bien configurados. Se crearon de nuevo utilizando bitbake-layers.
  
### References/Links
- https://github.com/openembedded/meta-openembedded 

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Date 19-9-2025 2

### Summary of Activity
-  Integración de los archivos necearios en Yocto para que la aplicación pueda correr en la máquina virtual. 

### Details/Observations
- La imagen se debe generar genericx86-64, no en qemux86. 

### Errores y soluciones
- No se encontraban los archivos.
- Solo se subían algunos archivos y otros no aparecían.
  S/ Se hizo una receta para cada archivo. 

### References/Links

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
  
## Date 21/22/23-9-2025 

### Summary of Activity
-  Validación de la funcionalidad total del programa dentro de una máquina virtual.   

### Details/Observations
- Desarrollo del resto del proyecto (documento tutorial). 

### Errores y soluciones
- La imagen no booteaba en VirtualBox.
  S/ Se debía cambiar algunas configuraciones en VirtualBox para permitir levantar el UEFI del sistema.

### References/Links

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
