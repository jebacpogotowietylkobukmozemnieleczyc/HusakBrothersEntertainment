#!/usr/bin/env python
from skimage import data
from matplotlib import pyplot as plt
from skimage import io
from skimage import filters
from skimage import feature;
from skimage import color;
from skimage import morphology;
import numpy as np

img_g = data.imread('samolot02.jpg', as_grey=True)

image = filters.sobel(img_g)
#image = feature.canny(image)



#image = data.lena() # Albo: coins(), page(), moon()
#image = color.rgb2grey(image)
image = morphology.dilation(image)
#image = morphology.dilation(image)
#image = filters.median(image, morphology.disk(5))
#image = morphology.erosion(image)
io.imshow(image)

plt.show()

# Niepotrzebne, jesli ipython notebook --matplotlib=inline
