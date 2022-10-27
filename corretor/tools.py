#!/usr/bin/python
#------------------------------------------------------------------------------#

# import fitz
import cv2
import io
import numpy as np

#------------------------------------------------------------------------------#
def pix_to_gray_image(pix):

    B = np.frombuffer(pix.samples, dtype=np.uint8)

    return B.reshape(pix.height, pix.width)

#------------------------------------------------------------------------------#

