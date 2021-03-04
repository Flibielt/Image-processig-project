import cv2
import os

from .grayscale_converter import GrayscaleConverter
from .util import show_image

grayscale_converter = GrayscaleConverter()


class Ocr:
    def __init__(self):
        self.image = None

    def read_image(self):
        self.image = cv2.imread("data/text.png", cv2.IMREAD_COLOR)

        return self.image

    def show_image(self):
        show_image(self.image, "Text")

    def save_image(self):
        home_dir = os.path.expanduser("~")
        file_path = os.path.join(home_dir, "Documents", "savedText.png")
        cv2.imwrite(file_path, self.image)

    def process_image(self):
        processed_image = grayscale_converter.process_image(self.image)
        show_image(processed_image, "Processed image")
