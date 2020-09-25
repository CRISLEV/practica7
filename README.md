# practica5sa
Practica #5 de laboratorio de Software Avanzado

Autor: Christian Gonzalez

Carnet: 200915168

##Requerimientos minimos de sistema
Python 3.8.3
Se utilizó el IDE Pycharm para desarrollar el proyecto.

##Versionamiento SemVer
Version 1.2.0

## Pasos para ejecutar el proyecto.
Ejecutar las clases principales de cada proyecto por separado:
	* Client.py
	* Restaurante.py
	* Repartidor.py
	* esb.py

Cada una se levantara en su respectivo puerto en el localhost.


## Development server
Estas son las diferentes rutas que se configuraron para cada proyecto.
	* CLIENTE: http://localhost:4100/
	* REPARTIDOR: http://localhost:4200/
	* RESTAURANTE: http://localhost:4300/
	* ESB: http://localhost:4400/


## Pasos para construir proyecto
En la carpeta de cada proyecto, ejecutar el siguiente comando:
	* python setup.py sdist

Este comando hara la construccion de artefactos por medio de compresion de archivos, ya que es codigo interpretado. 
El archivo .tar.gz esta ubicado en la carpeta /dist.
