# Automatizaci-n-de-Registro-de-Inventario-RPA-
Este proyecto consiste en un script de automatización desarrollado en Python optimiza el proceso de carga de productos en un sistema de gestión,lee una base de datos local y realiza el llenado automático de formularios web, eliminando el error humano y reduciendo drásticamente el tiempo de ejecución. 

1.El problema que vi y la solucion que le dí:


Problema: El registro manual de cientos de productos en un sistema web es una tarea repetitiva, lenta y propensa a errores de digitación.


Solución: Una automatización que integra la librería Pandas para procesar datos y PyAutoGUI para interactuar con la interfaz gráfica del usuario de forma autónoma.

2. Descripción Técnica (Paso a Paso)

Configuración del Entorno: Se establece un PAUSE de 1 segundo entre comandos para garantizar la estabilidad de la automatización.


Acceso al Sistema: El script inicia el navegador Chrome, navega a la URL de la empresa y realiza el login de forma automatizada. 

Procesamiento de Datos: Se utiliza Pandas para cargar el archivo ejemplochico.csv. El script recorre cada fila de la tabla de forma dinámica. 

Llenado Inteligente de Campos: Por cada producto, el script completa:

Código, Marca, Tipo y Categoría. 

Precios unitarios y costos de producción. 


Lógica Condicional: El script verifica si existen observaciones (obs) antes de escribirlas, evitando errores de datos nulos (NaN). 


Finalización: Tras registrar cada producto, el script hace scroll hacia arriba para reiniciar la posición visual y continuar con el siguiente registro.

Nota: Las coordenadas de clic (x, y) utilizadas en este script son específicas para una resolución de pantalla de monitor determinada. Para ejecutar este proyecto en otro equipo, se debe utilizar el script auxiliar de "obtener posición" incluido en el repositorio.

