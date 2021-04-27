import numpy as np
import cv2
from matplotlib import pyplot as plt

from .word import Word

SHOW_HISTOGRAMS = True


def get_word_borders(histogram):
    threshold = max(histogram) / 20
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
                word.image = image_row[0:row_height, columns[col_index]:columns[col_index + 1]]
                word.resized_image = cv2.resize(word.image, (64, 64))
                word.y = rows[row_index]
                word.x = columns[col_index]
                words.append(word)

        cv2.imshow("first", words[6].resized_image)
        print("x: " + str(words[10].x) + ", y: " + str(words[0].y))
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        return words
