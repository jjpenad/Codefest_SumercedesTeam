# Ciclon

Ciclon is a Python library for handling geographical images, specifically features like:

* **Obfuscate:** This library enables the users to change the transform matrix of the geographical image 
with translations over the x and y axis

* **Preview and Resize:** Contains mechanisms that allow users to preview an image to a size of 5% of its original dimensions

* **Image-Compression:** It allows developers to compress geographical images to a scale of 1/10, keeping their quality and pixel size without losing relevant information

## Installation

The first step to use this library is to clone this repo. Then, you will have to install the necessary dependencies for the library in order to work correctly. To do that, please execute the following command:

```
pip install rasterio 
```

There is another dependecy called gdal that will allow the library to do comprssion operations. In order to get this dependency, please follow the next steps:

1. If you have a Windows machine, you first have to install conda. To do that, please use the following website [Offical Anaconda Download](https://www.anaconda.com/products/distribution). 

2. After installing conda, you must execute this commmand:

```
conda install -c conda-forge gdal
```



