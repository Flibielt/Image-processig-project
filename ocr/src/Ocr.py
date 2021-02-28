import cv2
import os


class Ocr:
    def __init__(self):
        self.image = None

    def read_image(self):
        self.image = cv2.imread("ocr/src/data/text.png", cv2.IMREAD_COLOR)

    def show_image(self):
        cv2.imshow("Text", self.image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def save_image(self):
        home_dir = os.path.expanduser("~")
        file_path = os.path.join(home_dir, "Documents", "savedText.png")
        cv2.imwrite(file_path, self.image)
