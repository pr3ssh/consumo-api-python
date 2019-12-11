CONSUMO DE API CON PYTHON

Fecha: 25/04/2019
Duración: 4h

1. Consideraciones generales (python 3.6 o superior, diccionarios, debug, JSON, APIs de ejemplo) Practicar con los metodos get del los diccionarios

1-debug.py
1-dir.py
1-dicts.py
1-json.py
1-csvreader.py
1-csvwriter.py
1-dictwriter.py
1-list-comprehensions.py
1-lambda.py


2. Protocolo HTTP:
NO CODE
Verbos: (GET, POST, PUT, DELETE) httpbin.org
Códigos: https://httpstatuses.com/


3. Librerías (requests)
NO CODE
Otra urllib2 (Python2) que en Python3 es urllib.request y urllib.error. No la usamos por su sintaxis más tosca pero tiene operaciones interesantes con elementos de una url.


4. GET
4-get-html.py
4-get-json.py
response.ok or response.status_code
Enseñar body (text) de la respuesta
Usar la librería json con json.loads(response.text)
response.json() devuelve no un objeto sino un diccionario


5. GET con Args
5-get-with-args.py
Ejercicios con https://www.metaweather.com/api/
(los parámetros van en la url con una query ?q1=xxx&q2=yyy)
diccionario como args y enviarlo por requests.get(params=args)

6. POST
Hacer solo ejercicios en httpbin.org
(json=payload or data=json.dumps(payload))
json: post se encarga de serializarlos (y los guarda en data)
data: debes encargarte de serializarlo (y se guarda en data). Si no se serializa, se guarda en form


7. PUT and DELETE
NO CODE


8. Headers
Nos puede servir en la petición y en al respuesta
(Ver el ejemplo de consumo de la API de Brewdog https://punkapi.com/documentation/v2)
(Access Token en los encabezados de OAuth). Se envian a traves de dicciarios. headers=headers


9, Cookies (httpbin.org) get/post/put/delete(url, cookies=dict)
NO CODE
Visualizaremos las cookies en la siguiente sección


10. Sessions (httpbin.org) get/post/put/delete(url, sessions=dict
10-sessions.py
Generamos sesion para que luego podamos recuperar las cookies


11. Chunks
11-chunks.py
(para archivos muy pesados como imágenes) requests.get(url, stream=True) stream deja la conexión abierta para descargar el contenido luego


## Ejercicios
* Crear un CSV ordenado con el número de organizaciones dependientes de GOV.UK (https://www.gov.uk/api/organisations)
cmapos: name, web, childrens
* Realizar algo con los edificios de caracter monumental de Madrid: https://datos.madrid.es/portal/site/egob/menuitem.214413fe61bdd68a53318ba0a8a409a0/?vgnextoid=b07e0f7c5ff9e510VgnVCM1000008a4a900aRCRD


## Para entregar
* Generar un script que recupere los APODs (Astronomy Picture of the Day) del mes de la última semana de la NASA y la convierta en blanco y negro.
https://api.nasa.gov/api.html#apod

from wand.image import Image
with Image(filename='color.jpg') as img:
    img.type = 'grayscale';
    img.save(filename='grayscale.jpg')


## Repositorios
* Datos abiertos de Zaragoza: https://zaragoza.es/sede/portal/datos-abiertos/



#!/usr/bin/env python
# -*- coding: utf-8 -*-

## Referencias

* https://www.analyticslane.com/2018/07/16/archivos-json-con-python/
* https://www.youtube.com/watch?v=SD_gvyH8tLU&list=PLpOqH6AE0tNguX5SG8HpcD3lfmzWrIn9n&index=1
* https://opendata-ajuntament.barcelona.cat/es/api-cataleg
