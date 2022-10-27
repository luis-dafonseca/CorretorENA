#------------------------------------------------------------------------------#

import cv2
import numpy as np

from rects import Rects

#------------------------------------------------------------------------------#
def create_mask():

    R = Rects.full_page()
    w = R.x1
    h = R.y1

    mask = np.zeros( (h,w), dtype=np.uint8 )

    for R in Rects.masks():
        mask [ R.y0:R.y1, R.x0:R.x1 ] = 255

    return mask

#------------------------------------------------------------------------------#
class Registration:

    #--------------------------------------------------------------------------#
    def __init__( self, model ):
    
        (height, width) = model.shape 
        self.warp_shape = ( width, height )
        
        MAX_FEATURES = 5000
        orb_detector = cv2.ORB_create(MAX_FEATURES)
        self.detect  = orb_detector.detectAndCompute

        self.mask = create_mask()

        (self.kps_model, self.descs_model) = self.detect(model, self.mask)
        
        self.matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck = True)
        
    #--------------------------------------------------------------------------#
    def transform( self, image ):
        
        (self.kps_image, self.descs_image) = self.detect(image, self.mask)
        
        matches = self.matcher.match(self.descs_image, self.descs_model)
        
        matches = sorted( matches, key=lambda x: x.distance )
        
        KEEP_PERCENT = 0.9
        keep = int( len(matches) * KEEP_PERCENT )
        matches = matches[:keep]

        N = len(matches)
        
        pts_image = np.zeros((N, 2))
        pts_model = np.zeros((N, 2))
        
        for (ii,m) in enumerate(matches):
            pts_image[ii,:] = self.kps_image[m.queryIdx].pt
            pts_model[ii,:] = self.kps_model[m.trainIdx].pt
        
        (H,_) = cv2.findHomography( pts_image, pts_model, cv2.RANSAC )
        
        return cv2.warpPerspective( image, H, self.warp_shape )

#------------------------------------------------------------------------------#
