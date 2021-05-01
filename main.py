from ocr.src import Ocr


def main():
    ocr = Ocr()
    text = ocr.process_image("data/printed.jpg")
    # text = ocr.process_image("data/sample.png")
    print(text)


if __name__ == '__main__':
    main()
