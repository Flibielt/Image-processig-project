import os

import cv2

from .grayscale_converter import GrayscaleConverter
from .image_filter import ImageFilter
from .util import show_image, save_image
from .word_detector import WordDetector
from .word_recognition import WordRecognizing

grayscale_converter = GrayscaleConverter()
image_filter = ImageFilter()
word_detector = WordDetector()
word_recognizing = WordRecognizing()


class Ocr:
    def __init__(self):
        self.image = None

    def preprocess_image(self):
        grayscale_image = grayscale_converter.process_image(self.image)
        show_image("Grayscale image", grayscale_image)

        filtered_image = image_filter.filter_image(grayscale_image)
        show_image("Filtered image", filtered_image)

        return filtered_image

    def process_image(self, image_name):
        print("Processing image...")
        self.image = cv2.imread(image_name, cv2.IMREAD_COLOR)
        save_image("original", self.image)

        filtered_image = self.preprocess_image()

        words = word_detector.detect_words(filtered_image)

        text = word_recognizing.recognize_words(words)

        return text
