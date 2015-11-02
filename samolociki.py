#!/usr/bin/env python
from skimage import data
from matplotlib import pyplot as plt
from skimage import io
from skimage import filters
from skimage import feature
from skimage import color
from skimage import morphology
import numpy as np


def load(name):
    image = data.imread(name, as_grey=True)
    image = filters.sobel(image)
    image = feature.canny(image)
    image = morphology.dilation(image)
    return image
# image = morphology.erosion(image)
# image = data.lena() # Albo: coins(), page(), moon()
# image = color.rgb2grey(image)
# image = morphology.dilation(image)
# image = filters.median(image, morphology.disk(5))


image = load("samolot07.jpg")
image2 = load("samolot08.jpg")
image7 = np.concatenate((image, image2), axis=1)

image3 = load("samolot01.jpg")
image4 = load("samolot02.jpg")
image8 = np.concatenate((image3, image4), axis=1)

image5 = load("samolot17.jpg")
image6 = load("samolot10.jpg")
image6.resize(image5.shape)
image9 = np.concatenate((image5, image6), axis=1)

image10 = np.concatenate((image7, image8), axis=0)
image11 = np.concatenate((image10, image9), axis=0)
io.imshow(image11)

plt.show()

# Niepotrzebne, jesli ipython notebook --matplotlib=inline
