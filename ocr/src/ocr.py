import cv2

from .character_detector import CharacterDetector
from .grayscale_converter import GrayscaleConverter
from .image_filter import ImageFilter
from .util import show_image, save_image
from .character_recognition import CharacterRecognizing

grayscale_converter = GrayscaleConverter()
image_filter = ImageFilter()
character_detector = CharacterDetector()
character_recognizing = CharacterRecognizing()


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

        characters = character_detector.detect_characters(filtered_image)

        text = character_recognizing.recognize_characters(characters)

        return text
