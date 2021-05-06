from ocr.src import Ocr


def main():
    ocr = Ocr()
    text = ocr.process_image("data/fox_easy.png")
    # text = ocr.process_image("data/printed.jpg")
    # text = ocr.process_image("data/printed_3.png")
    # text = ocr.process_image("data/printed_4.png")
    print(text)


if __name__ == '__main__':
    main()
