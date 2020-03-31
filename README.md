# **SISTEMA DE INFORMACIÓN SOBRE LA OCUPACIÓN DE BUSES DEL TRANSPORTE PUBLICO.**

# Motivación

# Desarrollo
### Actualización 28-03-2020 21:20
After 5 hours of work, the team V4A achieved the following results:
- We reviewed several state-of-the-art projects. 
- We implemented an object recognition system, see the [video](https://gitlab.com/IsRaTiAl/v4c/-/blob/master/videos/video_metro.avi).

### Actualización 29-03-2020 15:00
- We reviewed some tracking algorithms and implemented a basic [code](https://gitlab.com/IsRaTiAl/v4c/-/blob/master/videos/tracking.py)
- We implemented a person recognition system (see the [code](https://gitlab.com/IsRaTiAl/v4c/-/blob/master/notebooks/yolo.ipynb)) and processed the following [video](https://gitlab.com/IsRaTiAl/v4c/-/blob/master/videos/video_metro2.avi), 

### Actualización 30-03-2020  10:00
- A draf of the presentation has been prepared, see the [presentation](https://gitlab.com/IsRaTiAl/v4c/-/blob/master/Slides/Sistema_de_informaci%C3%B3n_sobre_la_ocupaci%C3%B3n_de_buses.pdf) 
- A simple but effective design has been created, it has the purpose to embed a JetsonNano/Raspberry, a USB_camera, and a battery. 
![Image description](https://gitlab.com/IsRaTiAl/v4c/-/raw/master/Designs/Design1.jpeg)

### Actualización 30-03-2020 19:00
- We implemented a person recognition, tracking and counting.
<p align="center">
  <img src="https://gitlab.com/IsRaTiAl/v4c/-/raw/master/videos/gifs/track+countv1.gif">
</p>

### Actualización 31-03-2020 10:30
Se desarrollo una aplicación web.
<p align="center"> <img src="https://gitlab.com/IsRaTiAl/v4c/-/raw/master/videos/gifs/app_webv1.gif"></p>
Asimismo, una app para moviles el cual será para los usuarios.
<p align="center">
  <img WIDTH="200" HEIGHT="400" src="https://gitlab.com/IsRaTiAl/v4c/-/raw/master/videos/gifs/app_movilv1.gif">
</p>
El seguimiento y conteo de personas fue probado en situaciones con variaciones en luz y velocidad de las personas en abordaje y desembarco.
<p align="center">
  <img src="https://gitlab.com/IsRaTiAl/v4c/-/raw/master/videos/gifs/track+countv2.gif">
</p>

## Tecnologías utilizadas
### Herramientas, librerias y frameworks
```
OpenCV
Tensorflow 1.x
Keras
SolidWorks
```
### Recursos

* [PCDS](https://freesoft.dev/program/128588362) - Base de datos utilizada
* [Darkflow](https://github.com/thtrieu/darkflow) - Implementación de Yolo.v2 empleada
* [Object Detection and Tracking](https://github.com/yehengchen/Object-Detection-and-Tracking) - Algoritmo de tracking implementado 
* GoogleColab - La máquina virtual utilizada en los experimentos.

## Instalación
## Creditos
* Israel Raul Tiñini Alvarez
* Carlos Helsner Menacho Guerra
* Luis Josmar Suarez Loza 
* Sergio Samuel Flores Llanqu


## Agradecimientos
La solución implementada fue inspirada en los siguientes trabajos: 
* [Benchmark data and method for real-time people counting in cluttered scenes using depth sensors](https://arxiv.org/abs/1804.04339)
* [People Detection and Finding Attractive Areas by the use of Movement Detection Analysis and Deep Learning Approach](https://www.sciencedirect.com/science/article/pii/S1877050919311287)
* [Simple Online and Realtime Tracking](https://arxiv.org/abs/1602.00763)

## Licencia

The MIT License

Copyright (c) 2020 Vision 4 Cities (V4C)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
