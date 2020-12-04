from numpy import *
from matplotlib import pyplot as plt
from functions import dctmtx, blockproc
import cv2 as cv

cmap='gray'

I = cv.imread('lena.jpg', 0)
I2 = cv.normalize(I.astype(float64), None, 0., 1., cv.NORM_MINMAX)
T = dctmtx(8)
B = blockproc(I2, lambda x: T.dot(x).dot(T.T), 8, 8)
mask = zeros((8, 8))
for i in range(4): mask[i,:4-i] = 1
B2 = blockproc(B, lambda x: x*mask, 8, 8)
I2 = blockproc(B2, lambda x: T.T.dot(x).dot(T), 8, 8)

Ie = cv.imread('lena_eq.jpg', 0)
I22 = cv.normalize(Ie.astype(float64), None, 0., 1., cv.NORM_MINMAX)
B = blockproc(I22, lambda x: T.dot(x).dot(T.T), 8, 8)
B2 = blockproc(B, lambda x: x*mask, 8, 8)
I3 = blockproc(B2, lambda x: T.T.dot(x).dot(T), 8, 8)

plt.subplot(221)
plt.imshow(I, cmap=cmap)
plt.title('lena')
plt.subplot(222)
plt.imshow(I2, cmap=cmap)
plt.title('lenaDCT')
plt.subplot(223)
plt.imshow(Ie, cmap=cmap)
plt.title('lena_eq')
plt.subplot(224)
plt.imshow(I3, cmap=cmap)
plt.title('lena_eqDCT')
plt.show()