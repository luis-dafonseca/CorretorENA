#------------------------------------------------------------------------------#
'''Create a class to manege all Image Manipulations'''

import cv2
import numpy as np
import fitz

import grading.rectangles as rects

#------------------------------------------------------------------------------#
def pix_to_gray_image(pixmap: fitz.Pixmap) -> cv2.Mat:
    '''Convert a fitz pixmap to a OpenCV image'''

    image = np.frombuffer(pixmap.samples, dtype=np.uint8)

    return image.reshape(pixmap.height, pixmap.width)

#------------------------------------------------------------------------------#
class ImageManipulation:
    '''Class to manage image manipulations'''

    # Registration parameters
    MAX_FEATURES = 5000
    KEEP_PERCENT = 0.9

    #--------------------------------------------------------------------------#
    def __init__(self) -> None:
        '''Initialize the ImageManipulation class'''

        # Registration information
        self.warp_shape  = None
        self.detect      = None
        self.kps_model   = None
        self.descs_model = None
        self.matcher     = None

        # Warped image
        self.image = None

        # Registration mask
        self.mask = np.zeros(
            (rects.PAGE.height, rects.PAGE.width),
            dtype=np.uint8
        )

        rect = rects.REGISTRATION_MASK
        self.mask[rect.y0:rect.y1, rect.x0:rect.x1] = 255

        # Gray level threshold
        self.threshold  = 0
        self.background = 0

    #--------------------------------------------------------------------------#
    def set_model(self, model_pixmap: fitz.Pixmap) -> None:
        '''Sets the model image for registration'''

        model_image = pix_to_gray_image(model_pixmap)

        height, width = model_image.shape
        self.warp_shape = (width, height)

        orb_detector = cv2.ORB_create(ImageManipulation.MAX_FEATURES)
        self.detect  = orb_detector.detectAndCompute

        self.kps_model, self.descs_model = self.detect(model_image, self.mask)

        self.matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck = True)

    #--------------------------------------------------------------------------#
    def register_image(self, pixmap: fitz.Pixmap) -> cv2.Mat:
        '''Warp image to match model'''

        image = pix_to_gray_image(pixmap)

        kps_image, descs_image = self.detect(image, self.mask)

        matches = self.matcher.match(descs_image, self.descs_model)
        matches = sorted(matches, key=lambda x: x.distance)

        keep = int(len(matches) * ImageManipulation.KEEP_PERCENT)
        matches = matches[:keep]

        nn = len(matches)

        pts_image = np.zeros((nn, 2))
        pts_model = np.zeros((nn, 2))

        for ii, mm in enumerate(matches):
            pts_image[ii,:] = kps_image     [mm.queryIdx].pt
            pts_model[ii,:] = self.kps_model[mm.trainIdx].pt

        hh, _ = cv2.findHomography(pts_image, pts_model, cv2.RANSAC)

        self.image = cv2.warpPerspective(image, hh, self.warp_shape)

        self.update_threshold()

        return self.image

    #--------------------------------------------------------------------------#
    def update_threshold(self):
        '''Update values of threshold and background'''

        rect = rects.BACKGROUND
        back = np.mean(self.image[rect.y0:rect.y1, rect.x0:rect.x1])

        rect = rects.BACKGROUND_GRAY
        gray = np.mean(self.image[rect.y0:rect.y1, rect.x0:rect.x1])

        self.threshold  = (back + gray) / 2
        self.background = back / 255

    #--------------------------------------------------------------------------#
    def get_binary(self):
        '''Return a binary array'''

        return self.image < self.threshold

    #--------------------------------------------------------------------------#
    def get_jpg(self):
        '''Encode image to JPG and return an IO buffer'''

        _, buffer = cv2.imencode('.jpg', self.image)

        return buffer

    #--------------------------------------------------------------------------#
    def get_png(self):
        '''Encode image to PNG and return an IO buffer'''

        _, buffer = cv2.imencode('.png', self.image)

        return buffer

    #--------------------------------------------------------------------------#
    def bg_gray(self) -> int:
        '''Return the average background gray level'''

        return self.background

#------------------------------------------------------------------------------#
