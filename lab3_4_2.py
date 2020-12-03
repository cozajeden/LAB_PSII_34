import numpy as np
import scipy as sp
from scipy import fftpack
from functions import magic

#wyniki są zaokrąglone do 5 miejsc po przecniku w celu uzyskania wyników sformatowanych podobnie do tych z octave
if __name__ == "__main__":
    src = magic(3, complex)
    result_fft2 = np.fft.fft2(src).round(5)

    result_fft2x1 = np.fft.fft(np.fft.fft(src.T).T).round(5)

    result_dct2 = fftpack.dctn(src, 2, norm='ortho').round(5)

    result_dct2x1 = sp.fft.dct(sp.fft.dct(src.T, norm='ortho').T, norm='ortho').round(5)
    # DCT2 można wyznaczyć za pomocą DCT1

    print('Oryginał:\n', src)
    print('fft2:\n', result_fft2)
    print('fft2x1:\n', result_fft2x1)
    print('dct2:\n', result_dct2)
    print('dct2x1:\n', result_dct2x1)
    print(f'fft2==fft2x1 = {np.array_equal(result_fft2, result_fft2x1)}')
    print(f'dct2==dct2x1 = {np.array_equal(result_dct2, result_dct2x1)}')
