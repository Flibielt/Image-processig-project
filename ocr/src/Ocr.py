import cv2
import os

from .grayscale_converter import GrayscaleConverter
from .word_detector import WordDetector
from .image_filter import ImageFilter
from .util import show_image

grayscale_converter = GrayscaleConverter()
image_filter = ImageFilter()
word_detector = WordDetector()


class Ocr:
    def __init__(self):
        self.image = None

    def read_image(self):
        self.image = cv2.imread("data/text.png", cv2.IMREAD_COLOR)

        return self.image

    def show_image(self):
        show_image("Text", self.image)

    def save_image(self):
        home_dir = os.path.expanduser("~")
        file_path = os.path.join(home_dir, "Documents", "savedText.png")
        cv2.imwrite(file_path, self.image)

    def preprocess_image(self):
        grayscale_image = grayscale_converter.process_image(self.image)
        # show_image("Grayscale image", grayscale_image)

        filtered_image = image_filter.filter_image(grayscale_image)
        # show_image("Filtered image", filtered_image)

        cv2.imshow("Grayscale", grayscale_image)
        cv2.imshow("Filtered", filtered_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        word_detector.detect_words(filtered_image)
