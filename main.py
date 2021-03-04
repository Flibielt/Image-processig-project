from ocr.src import Ocr, GrayscaleConverter
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def main():
    ocr = Ocr()
    grayscale_converter = GrayscaleConverter()
    image = ocr.read_image()
    ocr.show_image()
    ocr.save_image()

    grayscale_converter.image = image
    grayscale_converter.to_gray_scale()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
