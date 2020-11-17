## Desafio

El dataset adjunto contiene 2017 proyectos Java, e información relacionada a sus dependencias externas; sus potenciales vulnerabilidades y las ya expuestas.

Desarrollar un server web con REST API, con el cual subir el dataset, entrenar el modelo y poder clasificar los proyectos según severidad de las vulnerabilidades.

Este server debe contener los siguientes endpoints:
POST /dataset: Endpoint para subir csv para datasets.
POST /train: Endpoint con todos los parámetros necesarios para entrenar en base a él(los) dataset(s) subidos.
GET /*: Endpoint(s) de muestreo de datos clasificados.
POST & GET /evaluate: Subir un nuevo caso, consultando la base de conocimiento y obtener la severidad correspondiente.

Adjuntar al código una breve descripción de la metodología aplicada para obtener el modelo.

