import numpy as np
import cv2
import math

from .util import THRESHOLD, show_image


class GrayscaleConverter:
    def __init__(self):
        self.image = None
        self.gray_levels = [0] * THRESHOLD

        self.create_lookup_table(THRESHOLD)

    def process_image(self, image):
        self.image = image
        gray_image = self.to_gray_scale()

        return self.binarize_gray_image(gray_image)

    def to_gray_scale(self):
        gray_trans = np.array([[[0.07, 0.72, 0.21]]])
        gray_image = cv2.convertScaleAbs(np.sum(self.image * gray_trans, axis=2))
        show_image("Gray", gray_image)

        return gray_image

    def binarize_gray_image(self, image):
        H, W = self.image.shape[:2]

        binarized_image = np.zeros((H, W, 1), np.uint8)

        for height in range(H):
            for width in range(W):
                binarized_image[height, width] = self.lookup_gray(image[height, width])

        return binarized_image

    def create_lookup_table(self, threshold):
        step = math.floor(255 / (threshold - 1))

        for x in range(0, threshold):
            threshold_value = step * x
            if threshold_value > 255:
                self.gray_levels[x] = 255
            else:
                self.gray_levels[x] = threshold_value

    def lookup_gray(self, original_gray):
        index = 0

        for threshold_index in range(1, len(self.gray_levels)):
            if original_gray >= self.gray_levels[threshold_index]:
                index = index + 1
            else:
                break

        return self.gray_levels[index]
