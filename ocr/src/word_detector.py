from matplotlib import pyplot as plt
import numpy as np

LOW_HIST_VALUE = 50
HIGH_HIST_VALUE = 150


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

        horizontal_hist = self.image.shape[1] - np.sum(self.image, axis=1) / 255

        plt.plot(horizontal_hist)
        plt.show()

        lines = []
        line_count = 0
        for index in range(1, len(horizontal_hist)):
            if horizontal_hist[index] < LOW_HIST_VALUE:
                if horizontal_hist[index - 1] > HIGH_HIST_VALUE or horizontal_hist[index + 1] > HIGH_HIST_VALUE:
                    lines[line_count] = index
                    line_count = line_count + 1

        return lines

    def get_cols(self, rows):
        """
        Returns the rectangles, which contains one-one word.

        :param rows: The rows indexes
        :return: the rectangles, which contains one-one word.
        """

        words = []
        word_count = 0
        for row in range(0, len(rows), 2):
            width = self.image.shape[1]
            image_row = self.image[rows[row]:rows[row + 1], 0:width]
            row_height = image_row.shape[0]
            vertical_hist = image_row.shape[0] - np.sum(image_row, axis=0) / 255

            columns = []
            column_count = 0
            for index in range(1, len(vertical_hist)):
                if vertical_hist[index] < LOW_HIST_VALUE:
                    if vertical_hist[index] > HIGH_HIST_VALUE or vertical_hist[index] > HIGH_HIST_VALUE:
                        columns[column_count] = index
                        column_count = column_count + 1

            for index in range(0, len(columns), 2):
                words[word_count] = image_row[row_height:row_height, columns[index]:columns[index + 1]]
                word_count = word_count + 1

        return words
