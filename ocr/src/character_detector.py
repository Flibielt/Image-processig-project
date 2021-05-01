import numpy as np
import cv2
from matplotlib import pyplot as plt

from .character import Character
from .Walsh import Walsh
from .config import get_config
from .util import save_image

SHOW_HISTOGRAMS = get_config("DEBUG", "Plot") == "YES"
walsh = Walsh()


class CharacterCut:
    def __init__(self):
        self.image = None
        self.x = 0
        self.y = 0


def get_character_borders(histogram):
    threshold = max(histogram) / 45
    border = []

    is_character = False
    for index in range(1, len(histogram) - 1):
        if histogram[index] > threshold:
            if not is_character:
                border.append(index)
                is_character = True

        elif is_character:
            border.append(index)
            is_character = False

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


def get_detected_character_border(histogram):
    threshold = max(histogram) * 0.001
    border = []

    for i in range(0, len(histogram)):
        if (histogram[i] > threshold):
            border.append(i)
            break

    for i in range(len(histogram) - 1, 0, -1):
        if (histogram[i] > threshold):
            border.append(i)
            break

    return border


def cut_image(image, orig_x, orig_y):
    """Cut the unnecessary parts of."""
    vertical_hist = calculate_vertical_histogram(image)
    horizontal_hist = calculate_horizontal_histogram(image)

    vertical_border = get_detected_character_border(vertical_hist)
    left = vertical_border[0]
    right = vertical_border[1]

    horizontal_border = get_detected_character_border(horizontal_hist)
    top = horizontal_border[0]
    bottom = horizontal_border[1]

    image_cut = image[top: bottom, left: right]
    character_cut = CharacterCut()
    character_cut.image = image_cut
    character_cut.x = orig_x + left
    character_cut.y = orig_y + top
    return character_cut


def create_space(x, y, width):
    """Creates character with space"""
    character = Character()
    character.text = " "
    character.image = np.zeros((int(width), int(width)), np.uint8)
    character.x = x
    character.y = y

    return character


def calculate_average_character_length(characters):
    sum_width = 0
    for character in characters:
        sum_width = sum_width + len(character.image[0])

    return sum_width / len(characters)


class CharacterDetector:
    def __init__(self):
        self.image = None

    def detect_characters(self, image):
        self.image = image

        rows = self.get_horizontal_lines()
        characters = self.get_cols(rows)
        average_width = calculate_average_character_length(characters)

        for i in range(1, len(characters)):
            distance = abs(characters[i].x - (characters[i - 1].x + len(characters[i - 1].image[0])))
            if distance > average_width and characters[i - 1].text != " ":
                characters.insert(i, create_space(characters[i - 1].x, characters[i - 1].y, average_width))

        return characters

    def detect_etalon_characters(self, image):
        self.image = image

        rows = self.get_horizontal_lines()
        characters = self.get_cols(rows)

        return characters

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

        return get_character_borders(horizontal_hist)

    def get_cols(self, rows):
        """
        Returns the rectangles, which contains one-one character.

        :param rows: The rows indexes
        :return: the rectangles, which contains one-one character.
        """

        characters = []
        for row_index in range(0, len(rows), 2):
            width = self.image.shape[1]
            if len(rows) == 1:
                height = self.image.shape[0]
                image_row = self.image[rows[row_index]:height, 0:width]
            else:
                image_row = self.image[rows[row_index]:rows[row_index + 1], 0:width]

            row_height = image_row.shape[0]

            vertical_hist = calculate_vertical_histogram(image_row)

            if SHOW_HISTOGRAMS:
                plt.plot(vertical_hist)
                plt.show()

            columns = get_character_borders(vertical_hist)

            columns_length = len(columns) - len(columns) % 2
            for col_index in range(0, columns_length, 2):
                character = Character()
                image = image_row[0:row_height, columns[col_index]:columns[col_index + 1]]
                try:
                    min_image = cut_image(image, columns[col_index], rows[row_index])

                    if min_image.image.shape[0] == 0 or min_image.image.shape[1] == 0:
                        continue
                except:
                    continue
                character.image = min_image.image
                character.resized_image = cv2.resize(min_image.image, (64, 64))
                character.y = min_image.y
                character.x = min_image.x
                character.feature_vector = walsh.generate_feature_vector(character.resized_image)
                characters.append(character)

        image_with_rectangles = self.image
        for i in range(0, len(characters)):
            height = len(characters[i].image)
            width = len(characters[i].image[0])
            start_point = (characters[i].x, characters[i].y)
            end_point = (characters[i].x + width, characters[i].y + height)

            color = (0, 255, 0)
            thickness = 1
            image_with_rectangles = cv2.rectangle(image_with_rectangles, start_point, end_point, color, thickness)
        cv2.imshow("Characters", image_with_rectangles)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        save_image("detectedCharacters", image_with_rectangles)

        return characters
