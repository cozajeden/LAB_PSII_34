from numpy import *
from scipy import fftpack
from threading import Thread, Lock, Event
from matplotlib import pyplot as plt
import tkinter as tk
import cv2 as cv
from typing_extensions import IntVar
from functions import blockproc
from CanvasOCV import CanvasOCV

class MyTk(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.lock = Lock()
        self.event = Event()
        self.imageOriginal = cv.imread('lena.jpg')
        self.frame = tk.Frame(self)
        self.frame.pack(fill=tk.BOTH, expand=True)
        self.sFrame = tk.Frame(self)
        self.sFrame.pack(fill=tk.BOTH, expand=True)
        self.canvasOriginal = CanvasOCV(self.frame)
        self.canvasOriginal.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.canvasOriginal.set_imageOCV(self.imageOriginal)
        self.canvasDCT = CanvasOCV(self.frame)
        self.canvasDCT.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.canvasError = CanvasOCV(self.frame)
        self.canvasError.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.slideVar = IntVar(self, 0)
        self.slide = tk.Scale(self.sFrame, variable=self.slideVar, )
        self.thread = Thread(name='Refreshing thread', target=self.loop, args=(self.lock, self.event), daemon=True)
        self.thread.start()
    
    def set_e(self, *args, **kwargs):
        self.event.set()
        
    def loop(self, lock: Lock, event: Event):
        while True:
            if event.wait():
                self.canvasDCT.set_imageOCV(self.imageOriginal)
                event.clear()

root = MyTk()
root.mainloop()
