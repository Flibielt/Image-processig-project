import cv2
import os


def show_image(text, image):
    cv2.imshow(text, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def save_image(name, image):
    home_dir = os.path.expanduser("~")
    file_path = os.path.join(home_dir, "Documents", name + ".png")
    cv2.imwrite(file_path, image)
