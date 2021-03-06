from ocr.src import Ocr


def main():
    ocr = Ocr()
    ocr.read_image()
    ocr.save_image()
    ocr.preprocess_image()


if __name__ == '__main__':
    main()
