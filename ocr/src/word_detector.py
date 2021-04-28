import numpy as np
import cv2
from matplotlib import pyplot as plt

from .word import Word
from .Walsh import Walsh
from .config import get_config

SHOW_HISTOGRAMS = get_config("DEBUG", "Plot") == "YES"
walsh = Walsh()


def get_word_borders(histogram):
    threshold = max(histogram) / 25
    border = []

    word = False
    for index in range(1, len(histogram) - 1):
        if histogram[index] > threshold:
            if not word:
                border.append(index)
                word = True

        elif word:
            border.append(index)
            word = False

    return border


def calculate_horizontal_histogram(image):
    im = 255 - image
    height, width = image.shape[:2]

    histogram = np.zeros(height)

    for y in range(1, height):
        for x in range(1, width):
            if im[y, x] > 10:
                histogram[y] = histogram[y] + 1

    return histogram


def calculate_vertical_histogram(image):
    im = 255 - image
    height, width = image.shape[:2]

    histogram = np.zeros(width)

    for x in range(1, width):
        for y in range(1, height):
            if im[y, x] > 3:
                histogram[x] = histogram[x] + 2

    return histogram


def cut_image(image):
    """Cut the unnecessary parts of."""
    height = len(image)
    width = len(image[0])

    top = 0
    bottom = height
    left = 0
    right = width
    if min(image[:, 0]) > 250:
        for y in range(0, height):
            if min(image[:, y]) < 250:
                top = y - 1
                break

    if min(image[:, height - 1]) > 250:
        for y in range(height - 1, 0, -1):
            if min(image[:, y]) < 250:
                bottom = y + 1
                break

    if min(image[0, :]) > 250:
        for x in range(0, width):
            if min(image[x, :]) < 250:
                left = x - 1
                break

    if min(image[width - 1, :]) > 250:
        for x in range(width - 1, 0, -1):
            if min(image[x, :]) < 250:
                right = x + 1
                break

    image_cut = image[top: bottom, left: right]
    return image_cut


class WordDetector:
    def __init__(self):
        self.image = None

    def detect_words(self, image):
        self.image = image

        rows = self.get_horizontal_lines()
        words = self.get_cols(rows)

        return words

    def get_horizontal_lines(self):
        """
        Returns the horizontal boundaries of the rows.

        Get the boundaries by the histogram of the image.
        :return: The boundaries of the rows
        """

        horizontal_hist = calculate_horizontal_histogram(self.image)

        if SHOW_HISTOGRAMS:
            plt.plot(horizontal_hist)
            plt.show()

        return get_word_borders(horizontal_hist)

    def get_cols(self, rows):
        """
        Returns the rectangles, which contains one-one word.

        :param rows: The rows indexes
        :return: the rectangles, which contains one-one word.
        """

        words = []
        for row_index in range(0, len(rows), 2):
            width = self.image.shape[1]
            image_row = self.image[rows[row_index]:rows[row_index + 1], 0:width]

            row_height = image_row.shape[0]

            vertical_hist = calculate_vertical_histogram(image_row)

            if SHOW_HISTOGRAMS:
                plt.plot(vertical_hist)
                plt.show()

            columns = get_word_borders(vertical_hist)

            for col_index in range(0, len(columns), 2):
                word = Word()
                image = image_row[0:row_height, columns[col_index]:columns[col_index + 1]]
                word.image = image
                word.resized_image = cv2.resize(word.image, (64, 64))
                word.y = rows[row_index]
                word.x = columns[col_index]
                word.feature_vector = walsh.generate_feature_vector(word.resized_image)
                words.append(word)

        image_with_rectangles = self.image
        for i in range(0, len(words)):
            height = len(words[i].image)
            width = len(words[i].image[0])
            start_point = (words[i].x, words[i].y)
            end_point = (words[i].x + width, words[i].y + height)

            color = (0, 255, 0)
            thickness = 2
            image_with_rectangles = cv2.rectangle(image_with_rectangles, start_point, end_point, color, thickness)
        cv2.imshow("Words", image_with_rectangles)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        return words
