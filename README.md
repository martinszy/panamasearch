# panamasearch
MediaParty 2016
https://hackdash.org/projects/57c19017d9284f016c047248

# Descripción
Conocemos varios periodistas de datos que a lo largo de su carrera acumulan pequeñas o grandes bases de datos de nombres de personas que vale la pena investigar.

Por ejemplo:

Cuando emergió la base de datos de Panama Papers, ha resultado muy difícil buscar si alguno de los nombres de esas bases de datos privadas están en la base de datos de PP (que tiene 1 millón de nombres).

En este proyecto haremos un programa que permite cargar una lista de nombres desde un archivo CSV, construye una estructura de datos que mide la distancia entre todos los nombres de la lista cargada y el millón de nombres de Panama Papers, y a todos los que tengan una distancia menor que un umbral (threshold), los graba en un archivo o incluso en la base de datos Neo4J para que el periodista de datos pueda avanzar la investigación.

Cómo usuario de ejemplo / caso de uso, contaremos con algunos de los datasets de Andy Tow.
Necesitamos ayuda escribiendo el código que produce el índice, la UI para subir los CSV, el código que inserta los resultados a Neo4J, dockerizando todo para que un usuario pueda levantar todo el sistema con un sólo comando.

#Instalación
Instalar Docker: https://docs.docker.com/engine/getstarted/step_one/#step-1-get-docker

###Desde Docker Hub

No necesitan bajar el código, hay una imagen publica en Docker Hub y la pueden obtener así:

`docker run -p 3000:3000 -d cubetto/panamasearch:v1`


###Imagen Local

`docker build -t panamasearch`
`docker run -p 3000:3000 -d panamasearch`


#Instalación sin docker
`git clone https://github.com/martinszy/panamasearch.git`

`cd panamasearch`

`mkvirtualenv panamasearch`

`pip install -r requirements.txt`

`./manage.py migrate`

`./manage.py runserver`

Para ejecutar el proceso offline de los csv:

(usando el python dentro del virtualenv)

`python manage.py processcsv`
