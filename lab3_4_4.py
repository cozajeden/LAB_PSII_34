from numpy import *
from matplotlib import pyplot as plt
from functions import dctmtx, blockproc
import cv2 as cv

I = cv.imread('lena.jpg', 0)
I2 = cv.normalize(I.astype(float64), None, 0., 1., cv.NORM_MINMAX)
T = dctmtx(8)
B = blockproc(I2, lambda x: T.dot(x).dot(T.T), 8, 8)
mask = zeros((8, 8))
for i in range(4): mask[i,:4-i] = 1
B2 = blockproc(B, lambda x: x*mask, 8, 8)
I2 = blockproc(B2, lambda x: T.T.dot(x).dot(T), 8, 8)

plt.subplot(121)
plt.imshow(I, cmap='gray')
plt.subplot(122)
plt.imshow(I2, cmap='gray')
plt.show()