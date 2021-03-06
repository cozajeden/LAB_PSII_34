from numpy import *
from scipy import fftpack
from matplotlib import pyplot as plt

# sygnały
x = arange(20)
a = sin(x/10*pi)
b = append(ones(10), ones(10) * -1)
c = linspace(0,1,10)
c = append(c, c)

# DFT
dfta = fftpack.fft(a)
dftb = fftpack.fft(b)
dftc = fftpack.fft(c)

# DCT
dcta = fftpack.dct(a)
dctb = fftpack.dct(b)
dctc = fftpack.dct(c)

# moduły transformat
moddfta = abs(dfta)
moddftb = abs(dftb)
moddftc = abs(dftc)

moddcta = abs(dcta)
moddctb = abs(dctb)
moddctc = abs(dctc)

# odwrotna DFT
idfta = fftpack.ifft(dfta)
idftb = fftpack.ifft(dftb)
idftc = fftpack.ifft(dftc)

# odwrotna DCT
idcta = fftpack.idct(dcta)
idctb = fftpack.idct(dctb)
idctc = fftpack.idct(dctc)

# Wyswietlanie wykresów
plt.figure(0)
plt.subplot(321)
plt.stem(x, a)
plt.title('a')
plt.subplot(323)
plt.stem(x, moddfta)
plt.title('moduł dft a')
plt.subplot(325)
plt.stem(x, idfta)
plt.title('idft a')
plt.subplot(324)
plt.stem(x, moddcta)
plt.title('moduł dct a')
plt.subplot(326)
plt.stem(x, idcta)
plt.title('idct a')
plt.tight_layout()

plt.figure(1)
plt.subplot(321)
plt.stem(x, b)
plt.title('b')
plt.subplot(323)
plt.stem(x, moddftb)
plt.title('moduł dft b')
plt.subplot(325)
plt.stem(x, idftb)
plt.title('idft b')
plt.subplot(324)
plt.stem(x, moddctb)
plt.title('moduł dct b')
plt.subplot(326)
plt.stem(x, idctb)
plt.title('idct b')
plt.tight_layout()

plt.figure(2)
plt.subplot(321)
plt.stem(x, c)
plt.title('c')
plt.subplot(323)
plt.stem(x, moddftc)
plt.title('moduł dft c')
plt.subplot(325)
plt.stem(x, idftc)
plt.title('idft c')
plt.subplot(324)
plt.stem(x, moddctc)
plt.title('moduł dct c')
plt.subplot(326)
plt.stem(x, idctc)
plt.title('idct c')
plt.tight_layout()


plt.show()