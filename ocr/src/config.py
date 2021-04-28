import configparser


def get_config(section, key):
    config = configparser.ConfigParser()
    config.read('ocr.ini')

    try:
        return config[section][key]
    except:
        return ""
