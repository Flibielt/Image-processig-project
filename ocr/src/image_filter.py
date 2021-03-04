import math


class ImageFilter:
    def __init__(self):
        self.image = None

    def filter_image(self, image):
        self.image = image
        image_height, image_width = self.image.shape[:2]

        for height in range(1, image_height):
            for width in range(1, image_width):
                if self.is_isolated_pixel(height, width):
                    self.image[height, width] = self.average_filter(height, width)
                else:
                    self.image[height, width] = self.image[height, width]

        return self.image

    def is_isolated_pixel(self, pixel_y, pixel_x):
        pixel = self.image[pixel_y, pixel_x]
        different_pixel_count = 0

        for height in range(pixel_y - 1, pixel_y + 1):
            for width in range(pixel_x - 1, pixel_x + 1):
                if self.image[height, width] != pixel:
                    different_pixel_count = different_pixel_count + 1

        if different_pixel_count == 8:
            return True
        return False

    def average_filter(self, pixel_y, pixel_x):
        pixel_sum = 0

        for height in range(pixel_y - 1, pixel_y + 1):
            for width in range(pixel_x - 1, pixel_x + 1):
                pixel_sum = pixel_sum + self.image[height, width]

        return math.floor(pixel_sum / 9)
