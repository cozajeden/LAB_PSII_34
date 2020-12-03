from tkinter import *
from tkinter import filedialog
from numpy import *
import numpy as np
from scipy import fftpack
from threading import Thread, Event, Lock
import cv2 as cv
from functions import blockproc
from CanvasOCV import CanvasOCV

class MyTk(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Otwarcie obrazu
        self.imageOriginal = cv.imread('lena_eq.jpg', 0)

        # Ramki
        self.lFrame = Frame(self)
        self.lFrame.pack(side=TOP, fill=BOTH, expand=True)
        self.frame = Frame(self)
        self.frame.pack(side=TOP, fill=BOTH, expand=True)
        self.sFrame = Frame(self)
        self.sFrame.pack(side=TOP, fill=BOTH, expand=True)
        self.cFrame = Frame(self)
        self.cFrame.pack(side=TOP, fill=BOTH, expand=True)

        # Etykiety
        font = 'Halvetica 24'
        self.lOrigional = Label(self.lFrame, text='Oryginał', font=font)
        self.lCompressed = Label(self.lFrame, text='Kompresja', font=font)
        self.lError = Label(self.lFrame, text='Błąd', font=font)
        self.lCoefficientVar = StringVar(self, '')
        self.lCoefficient = Label(self.cFrame, textvariable=self.lCoefficientVar, font=font)
        self.lOrigional.pack(side=LEFT, fill=BOTH, expand=1)
        self.lCompressed.pack(side=LEFT, fill=BOTH, expand=1)
        self.lError.pack(side=LEFT, fill=BOTH, expand=1)
        self.lCoefficient.pack(side=TOP, fill=BOTH, expand = 1)

        # Obrazy
        self.canvasOriginal = CanvasOCV(self.frame)
        self.canvasOriginal.pack(side=LEFT, fill=BOTH, expand=True)
        self.canvasOriginal.set_imageOCV(self.imageOriginal)
        self.canvasDCT = CanvasOCV(self.frame)
        self.canvasDCT.pack(side=LEFT, fill=BOTH, expand=True)
        self.canvasError = CanvasOCV(self.frame)
        self.canvasError.pack(side=LEFT, fill=BOTH, expand=True)

        # Sówak
        self.slideVar = DoubleVar(self, 0)
        self.slide = Scale(self.sFrame, variable=self.slideVar, from_=0, to=1, resolution=0.0001, orient=HORIZONTAL, command=self.refresh)
        self.slide.pack(side=TOP, fill=BOTH, expand = 1)

        # Przycisk
        self.button = Button(self.cFrame, text='Wybierz obraz', bg='lightblue', font=font, command=self.choose_image)
        self.button.pack(side=TOP, fill=BOTH, expand = 1)

        # Inicjacja osobnego wątku obliczeniowego
        self.var = 0
        self.event = Event()
        self.thread = Thread(name='Refreshing thread', target=self.loop, args=(self.event,), daemon=True)
        self.thread.start()
        self.event.set()

    def choose_image(self):
        "Ładowanie obrazu z pliku"
        path = filedialog.askopenfilename()
        if path is not None:
            self.imageOriginal = cv.imread(path, 0)
            self.canvasOriginal.set_imageOCV(self.imageOriginal)
            self.event.set()
    
    def refresh(self, *args, **kwargs):
        "Event zmiany wartości sówaka."
        self.var = self.slideVar.get()
        self.event.set()
        
    def loop(self, event: Event):
        "W tej funkcji znajdują się wszystkie obliczenia."
        while True:
            # Czekaj na zmianę wartości sówaka
            if event.wait():
                # Wyczyść evant zmiany wartości sówaka
                event.clear()

                # Zastosuj DCT w blokach 8x8
                dctIm = blockproc(self.imageOriginal, lambda x: fftpack.dctn(x, 2, norm='ortho'), 8, 8)
                thresh = self.var
                
                # Zastosuj threshold
                dctIm[abs(dctIm) < thresh*np.max(abs(dctIm))] = 0

                # Zastosuj odwrotne DCT w blokach 8x8
                idctIm = blockproc(dctIm, lambda x: fftpack.idctn(x, 2, norm='ortho'), 8, 8)

                # Wyświetl skompresoawne zdjęcie
                self.canvasDCT.set_imageOCV(idctIm)

                # Oblicz i wyświetl różnice pomiędzy oryginałem i zdjęciem skompresowanym
                errIm = abs(self.imageOriginal - idctIm).astype(uint8)
                self.canvasError.set_imageOCV(errIm)

                # Oblicz i wyswietl % użytych współczynników
                coe = 100 - 100 * float(np.sum(abs(dctIm) < thresh*np.max(abs(dctIm)))) / float(dctIm.shape[0] * dctIm.shape[1])
                self.lCoefficientVar.set(f'Użyto {coe:0.4f}% współczynników.')

root = MyTk()
root.mainloop()
