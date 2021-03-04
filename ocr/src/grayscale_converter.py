import numpy as np
import cv2
import math


class GrayscaleConverter:
    def __init__(self):
        self.image = None

    def to_gray_scale(self):
        gray_trans = np.array([[[0.07, 0.72, 0.21]]])
        gray_image = cv2.convertScaleAbs(np.sum(self.image * gray_trans, axis=2))
        cv2.imshow("Gray", gray_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        return gray_image

    def binarize_gray_image(self, image, threshold):
        H, W = self.image.shape[:2]

        binarized_image = np.zeros((H, W))

    def lookup_gray(self, original_gray, threshold):
        gray_levels = []
        for x in range(threshold):
            gray_levels[x] = math.floor(255 / x)

