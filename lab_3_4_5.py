from cv2 import cv2 as cv
from pathlib import Path

if __name__ == "__main__":
    image_jpg = cv.imread('lena.jpg')
    cv.imwrite(img=image_jpg, filename='lena.bmp')
    cv.imwrite(img=image_jpg, filename='lena.tiff')

    jpg_file = Path("lena.jpg")
    bmp_file = Path("lena.bmp")
    tiff_file = Path("lena.tiff")
    print(f'lena.jpg: {jpg_file.stat().st_size/1024:.02f}kB, \nlena.bmp: {bmp_file.stat().st_size/1024:.02f}kB, \nlena.tiff: {tiff_file.stat().st_size/1024:.02f}kB')

    image_jpg = cv.imread('lena_eq.jpg')
    cv.imwrite(img=image_jpg, filename='lena_eq.bmp')
    cv.imwrite(img=image_jpg, filename='lena_eq.tiff')

    jpg_file = Path("lena_eq.jpg")
    bmp_file = Path("lena_eq.bmp")
    tiff_file = Path("lena_eq.tiff")
    print(f'lena_eq.jpg: {jpg_file.stat().st_size/1024:.02f}kB, \nlena_eq.bmp: {bmp_file.stat().st_size/1024:.02f}kB, \nlena_eq.tiff: {tiff_file.stat().st_size/1024:.02f}kB')