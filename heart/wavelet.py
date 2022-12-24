import numpy as np
import pywt
import cv2


def w2d(img, mode='haar', level=1):
    im_array = img
    im_array = cv2.cvtColor(im_array, cv2.COLOR_RGB2GRAY)
    im_array = np.float32(im_array)
    im_array /= 255
    coeffs = pywt.wavedec2(im_array, mode, level=level)

    coeffs_H = list(coeffs)
    coeffs_H[0] *= 0

    imArray_H = pywt.waverec2(coeffs_H, mode)
    imArray_H *= 255
    imArray_H = np.uint8(imArray_H)

    return imArray_H
