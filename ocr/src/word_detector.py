from matplotlib import pyplot as plt
import numpy as np
import cv2


def get_word_borders(histogram, threshold):
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
        self.get_cols(rows)

    def get_horizontal_lines(self):
        """
        Returns the horizontal boundaries of the rows.

        Get the boundaries by the histogram of the image.
        :return: The boundaries of the rows
        """

        horizontal_hist = calculate_horizontal_histogram(self.image)

        # plt.plot(horizontal_hist)
        # plt.show()

        return get_word_borders(horizontal_hist, 40)

    def get_cols(self, rows):
        """
        Returns the rectangles, which contains one-one word.

        :param rows: The rows indexes
        :return: the rectangles, which contains one-one word.
        """

        words = []
        for row in range(0, len(rows), 2):
            width = self.image.shape[1]
            image_row = self.image[rows[row]:rows[row + 1], 0:width]

            cv2.imshow("row", image_row)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

            row_height = image_row.shape[0]

            vertical_hist = calculate_vertical_histogram(image_row)

            columns = get_word_borders(vertical_hist, 3)

            plt.plot(vertical_hist)
            plt.show()

            for index in range(0, len(columns), 2):
                words.append(image_row[0:row_height, columns[index]:columns[index + 1]])

        cv2.imshow("first", words[0])
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        return words
