from cv2 import cv2 as cv
from pathlib import Path

if __name__ == "__main__":
    image_jpg = cv.imread('lena.jpg')
    cv.imwrite(img=image_jpg, filename='lena.bmp')
    cv.imwrite(img=image_jpg, filename='lena.tiff')

    jpg_file = Path("lena.jpg")
    bmp_file = Path("lena.bmp")
    tiff_file = Path("lena.tiff")
    print(f'jpg: {jpg_file.stat().st_size}, \nbmp: {bmp_file.stat().st_size}, \ntiff: {tiff_file.stat().st_size}')

