# **Sistema de información sobre la ocupación de buses del transporte publico.**

In this work, we implement an intelligent system to count the number of people getting on in a bus. 

## Update March 28, 2020 21:20
After 5 hours of work, the team V4A achieved the following results:
- We reviewed several state-of-the-art projects. 
- We implemented an object recognition system, see the [video](https://gitlab.com/IsRaTiAl/v4c/-/blob/master/videos/video_metro.avi).

## Update March 29, 2020 15:00
- We reviewed some tracking algorithms and implemented a basic [code](https://gitlab.com/IsRaTiAl/v4c/-/blob/master/videos/tracking.py)
- We implemented a person recognition system (see the [code](https://gitlab.com/IsRaTiAl/v4c/-/blob/master/notebooks/yolo.ipynb)) and processed the following [video](https://gitlab.com/IsRaTiAl/v4c/-/blob/master/video_metro2.avi), 

## Update March 30, 2020 10:00
- A draf of the presentation has been prepared, see the [presentation](https://gitlab.com/IsRaTiAl/v4c/-/blob/master/Slides/Sistema_de_informaci%C3%B3n_sobre_la_ocupaci%C3%B3n_de_buses.pdf) 
- A simple but effective design has been created, it has the purpose to embed a JetsonNano/Raspberry, a USB_camera, and a battery. 
![Image description](https://gitlab.com/IsRaTiAl/v4c/-/raw/master/Design1.jpeg)
## Tools
This project has been build using the following tools:
```
OpenCV
Tensorflow 1.x
Keras
SolidWorks
```

## Resources

* [PCDS](https://freesoft.dev/program/128588362) - The dataset used
* [Darkflow](https://github.com/thtrieu/darkflow) - Yolov2 implementation in Python
* GoogleColab - The virtual machine used in the experiments 

## Acknowledgments
This work has been inspired on: 
* [Benchmark data and method for real-time people counting in cluttered scenes using depth sensors](https://arxiv.org/abs/1804.04339)
* [People Detection and Finding Attractive Areas by the use of Movement Detection Analysis and Deep Learning Approach](https://www.sciencedirect.com/science/article/pii/S1877050919311287)
