import cv2
import string
import configparser
from .word_detector import WordDetector

ETALON_IMAGE = "data/etalon.png"
word_detector = WordDetector()
USER_INPUT = False

config = configparser.ConfigParser()
config.read('ocr.ini')
try:
    value = config["ETALON"]["UserInput"]
    USER_INPUT = value == "YES"
except:
    USER_INPUT = False


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
        self.etalon_matrix = word_detector.detect_words(ETALON_IMAGE)

        if USER_INPUT:
            print("Please give the character which can be seen on the images.")
            for i in range(0, len(self.etalon_matrix)):
                cv2.imshow("Word", self.etalon_matrix[i].resized_image)
                character = input("The character: ")
                self.etalon_matrix[i].text = character
        for i in range(0, len(self.etalon_matrix)):
            if i < len(ETALON_TEXT):
                self.etalon_matrix[i].text = ETALON_TEXT[i]
