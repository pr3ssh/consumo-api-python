CONSUMO DE API CON PYTHON
=========================

Fecha: 25/04/2019
Duración: 4h

## Consideraciones generales (python 3.6 o superior, diccionarios, debug, JSON, APIs de ejemplo) Practicar con los metodos get del los diccionarios

* 1-debug.py
* 1-dir.py
* 1-dicts.py
* 1-json.py
* 1-csvreader.py
* 1-csvwriter.py
* 1-dictwriter.py
* 1-list-comprehensions.py
* 1-lambda.py


## Protocolo HTTP:

NO CODE

Verbos: (GET, POST, PUT, DELETE) httpbin.org

Códigos: https://httpstatuses.com/


## Librerías (requests)

NO CODE

Otra urllib2 (Python2) que en Python3 es urllib.request y urllib.error. No la usamos por su sintaxis más tosca pero tiene operaciones interesantes con elementos de una url.


## GET

* 4-get-html.py
* 4-get-json.py

response.ok or response.status_code

Enseñar body (text) de la respuesta

Usar la librería json con json.loads(response.text)

response.json() devuelve no un objeto sino un diccionario


## GET con Args

* 5-get-with-args.py

Ejercicios con https://www.metaweather.com/api/ (los parámetros van en la url con una query ?q1=xxx&q2=yyy o diccionario como args y enviarlo por requests.get(params=args)

## POST

Hacer solo ejercicios en httpbin.org

(json=payload or data=json.dumps(payload))

* json: post se encarga de serializarlos (y los guarda en data)
* data: debes encargarte de serializarlo (y se guarda en data). Si no se serializa, se guarda en form


## PUT and DELETE

NO CODE


## Headers

Nos puede servir en la petición y en al respuesta

(Ver el ejemplo de consumo de la API de Brewdog https://punkapi.com/documentation/v2)

(Access Token en los encabezados de OAuth). Se envian a traves de dicciarios. headers=headers


## Cookies (httpbin.org) get/post/put/delete(url, cookies=dict)

NO CODE

Visualizaremos las cookies en la siguiente sección


## Sessions (httpbin.org) get/post/put/delete(url, sessions=dict

* 10-sessions.py

Generamos sesion para que luego podamos recuperar las cookies


## Chunks

* 11-chunks.py

(para archivos muy pesados como imágenes) requests.get(url, stream=True) stream deja la conexión abierta para descargar el contenido luego


## Ejercicios

* Crear un CSV ordenado con el número de organizaciones dependientes de GOV.UK (https://www.gov.uk/api/organisations) // campos: name, web, childrens
* Realizar alguna visualización con los edificios de caracter monumental de Madrid: https://datos.madrid.es/portal/site/egob/menuitem.214413fe61bdd68a53318ba0a8a409a0/?vgnextoid=b07e0f7c5ff9e510VgnVCM1000008a4a900aRCRD


## Para entregar

* Generar un script que recupere los APODs (Astronomy Picture of the Day) del mes de la última semana de la NASA y la convierta en blanco y negro.
https://api.nasa.gov/api.html#apod

```
from wand.image import Image
with Image(filename='color.jpg') as img:
    img.type = 'grayscale';
    img.save(filename='grayscale.jpg')
```
