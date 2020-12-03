import numpy as np
import scipy as sp
from functions import magic

#wyniki są zaokrąglone do 5 miejsc po przecniku w celu uzyskania wyników sformatowanych podobnie do tych z octave
if __name__ == "__main__":
    src = magic(3, complex)
    result_fft2 = np.fft.fft2(src).round(5)

    # result_fft = np.zeros((3, 3), complex)
    # for row in range(len(src)):
    #     result_fft[row] = np.fft.fft(src[row])
    # result_fft = result_fft.T
    # for row in range(len(result_fft)):
    #     result_fft[row] = np.fft.fft(result_fft[row])
    # result_fft = result_fft.T
    result_fft = np.fft.fft(np.fft.fft(src.T).T).round(5)

    result_dct2 = sp.fft.dct(sp.fft.dct(src.T, norm='ortho').T, norm='ortho').round(5)
    # DCT2 można wyznaczyć za pomocą DCT1 - prezentacja przykładu na górze (bo dct2 nie ma)
