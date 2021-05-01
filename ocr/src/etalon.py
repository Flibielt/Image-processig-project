import cv2
import string

from .word_detector import WordDetector
from .grayscale_converter import GrayscaleConverter
from .config import get_config

ETALON_IMAGE_PATH = "data/etalon.png"
word_detector = WordDetector()
USER_INPUT = get_config("ETALON", "UserInput") == "YES"

grayscale_converter = GrayscaleConverter()


def create_etalon_text():
    etalon_text = string.ascii_lowercase + string.ascii_uppercase

    for i in range(0, 10):
        etalon_text = etalon_text + str(i)

    return etalon_text


ETALON_TEXT = create_etalon_text()


class Etalon:
    def __init__(self):
        self.etalon_matrix = None
        self.etalon_text = create_etalon_text()

    def create_etalon_matrix(self):
        etalon_image = cv2.imread(ETALON_IMAGE_PATH, cv2.IMREAD_COLOR)
        etalon_image_grayscale = grayscale_converter.process_image(etalon_image)
        self.etalon_matrix = word_detector.detect_etalon_words(etalon_image_grayscale)

        if USER_INPUT:
            print("Please give the character which can be seen on the images.")
            for i in range(0, len(self.etalon_matrix)):
                cv2.imshow("Word", self.etalon_matrix[i].resized_image)
                character = input("The character: ")
                self.etalon_matrix[i].text = character
        for i in range(0, len(self.etalon_matrix)):
            if i < len(ETALON_TEXT):
                self.etalon_matrix[i].text = ETALON_TEXT[i]
