import numpy as np
import cv2

THRESHOLD = 2


class GrayscaleConverter:
    def __init__(self):
        self.image = None
        self.gray_levels = [0] * THRESHOLD
        self.threshold = 0

        self.create_lookup_table()

    def process_image(self, image):
        self.image = image
        gray_image = self.to_gray_scale()

        return self.binarize_gray_image(gray_image)

    def to_gray_scale(self):
        gray_trans = np.array([[[0.07, 0.72, 0.21]]])
        gray_image = cv2.convertScaleAbs(np.sum(self.image * gray_trans, axis=2))

        self.threshold = np.mean(gray_image) - 33

        return gray_image

    def binarize_gray_image(self, image):
        H, W = self.image.shape[:2]

        binarized_image = np.zeros((H, W, 1), np.uint8)

        for height in range(H):
            for width in range(W):
                binarized_image[height, width] = self.lookup_gray(image[height, width])

        return binarized_image

    def create_lookup_table(self):
        """
        for x in range(0, THRESHOLD):
            threshold_value = step * x
            if threshold_value > 255:
                self.gray_levels[x] = 255
            else:
                self.gray_levels[x] = threshold_value
        """
        self.gray_levels[0] = 0
        self.gray_levels[1] = 255

    def lookup_gray(self, original_gray):
        if self.threshold > original_gray:
            return 0
        else:
            return 255
