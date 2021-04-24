import os

import cv2

from .grayscale_converter import GrayscaleConverter
from .image_filter import ImageFilter
from .word_detector import WordDetector

grayscale_converter = GrayscaleConverter()
image_filter = ImageFilter()
word_detector = WordDetector()


class Ocr:
    def __init__(self):
        self.image = None

    def save_image(self):
        home_dir = os.path.expanduser("~")
        file_path = os.path.join(home_dir, "Documents", "savedText.png")
        cv2.imwrite(file_path, self.image)

    def preprocess_image(self):
        grayscale_image = grayscale_converter.process_image(self.image)
        # show_image("Grayscale image", grayscale_image)

        filtered_image = image_filter.filter_image(grayscale_image)
        # show_image("Filtered image", filtered_image)

        return filtered_image

    def process_image(self, image_name):
        print("Processing image...")
        self.image = cv2.imread(image_name, cv2.IMREAD_COLOR)
        self.save_image()

        filtered_image = self.preprocess_image()

        word_detector.detect_words(filtered_image)

        return "Patience"