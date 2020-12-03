from numpy import *
from scipy import fftpack
from matplotlib import pyplot as plt

x = arange(20)
a = sin(x/10*pi)
b = append(ones(10), zeros(10))
c = linspace(0,1,10)
c = append(c, c)

dfta = fftpack.fft(a)
dftb = fftpack.fft(b)
dftc = fftpack.fft(c)

dcta = fftpack.dct(a)
dctb = fftpack.dct(b)
dctc = fftpack.dct(c)

moddfta = abs(dfta)
moddftb = abs(dftb)
moddftc = abs(dftc)

moddcta = abs(dcta)
moddctb = abs(dctb)
moddctc = abs(dctc)

idfta = fftpack.ifft(dfta)
idftb = fftpack.ifft(dftb)
idftc = fftpack.ifft(dftc)

idcta = fftpack.idct(dcta)
idctb = fftpack.idct(dctb)
idctc = fftpack.idct(dctc)

plt.figure(0)
plt.subplot(421)
plt.stem(x, a)
plt.title('a')
plt.subplot(423)
plt.stem(x, dfta)
plt.title('dft a')
plt.subplot(425)
plt.stem(x, moddfta)
plt.title('moduł dft a')
plt.subplot(427)
plt.stem(x, idfta)
plt.title('idft a')
plt.subplot(424)
plt.stem(x, dcta)
plt.title('dct a')
plt.subplot(426)
plt.stem(x, moddcta)
plt.title('moduł dct a')
plt.subplot(428)
plt.stem(x, idcta)
plt.title('idct a')

plt.figure(1)
plt.subplot(421)
plt.stem(x, b)
plt.title('b')
plt.subplot(423)
plt.stem(x, dftb)
plt.title('dft b')
plt.subplot(425)
plt.stem(x, moddftb)
plt.title('moduł dft b')
plt.subplot(427)
plt.stem(x, idftb)
plt.title('idft b')
plt.subplot(424)
plt.stem(x, dctb)
plt.title('dct b')
plt.subplot(426)
plt.stem(x, moddctb)
plt.title('moduł dct b')
plt.subplot(428)
plt.stem(x, idctb)
plt.title('idct b')

plt.figure(2)
plt.subplot(421)
plt.stem(x, c)
plt.title('c')
plt.subplot(423)
plt.stem(x, dftc)
plt.title('dft c')
plt.subplot(425)
plt.stem(x, moddftc)
plt.title('moduł dft c')
plt.subplot(427)
plt.stem(x, idftc)
plt.title('idft c')
plt.subplot(424)
plt.stem(x, dctc)
plt.title('dct c')
plt.subplot(426)
plt.stem(x, moddctc)
plt.title('moduł dct c')
plt.subplot(428)
plt.stem(x, idctc)
plt.title('idct c')


plt.tight_layout()
plt.show()