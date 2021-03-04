import cv2

THRESHOLD = 3


def show_image(image, text):
    cv2.imshow(text, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()