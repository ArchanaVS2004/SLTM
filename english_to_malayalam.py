"""
Program to translate english to malayalam.

Uses Google translator.
"""
from googletrans import Translator


class EnglishToMalayalam:
    """English to malayalam object class."""

    def __init__(self) -> None:
        """Initialize attributes."""

    @staticmethod
    def write_file(file, sentence):
        """Write the sentence to file."""
        file.write(sentence)
        file.write("\n")
        return file.tell()

    @staticmethod
    def read_file(file, file_index=0):
        """Read the file."""
        file.seek(file_index)
        return file.readline()

    @staticmethod
    # def translate_file(org_file, trans_file):
    def translate_file(org_file, file_index):
        """Translate the sentence to malayalam."""
        translator = Translator()
        sentence = EnglishToMalayalam.read_file(org_file, file_index)
        translate_word = translator.translate(sentence, dest="ml")
        print(f'Translation: {translate_word.text}')
        file_index = EnglishToMalayalam.write_file(
            org_file, translate_word.text)
        return file_index


def error_handler(func):
    """Error handling decortor."""
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyboardInterrupt:
            print("Translation completed")
    return wrapper


@error_handler
def main():
    """Program start here."""
    filename = "chat_translator.txt"
    english_malayalam = EnglishToMalayalam()
    file_index_list = [0]
    with open(filename, mode='a+', encoding='UTF-8') as my_file:
        while True:
            sentence = input("Enter the sentence:")
            file_index = english_malayalam.write_file(my_file, sentence)
            file_index_list.append(file_index)
            file_index = english_malayalam.translate_file(
                my_file, file_index_list.pop(0))
            file_index_list.append(file_index)
            file_index_list.pop(0)  # Poping the data from index 0


if __name__ == '__main__':
    main()
