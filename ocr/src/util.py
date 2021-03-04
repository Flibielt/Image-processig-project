import cv2

THRESHOLD = 10


def show_image(text, image):
    cv2.imshow(text, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
