def get_file_content(filename='text.txt'):
    """ Reads content of given text file and return it as string. """
    with open(filename, 'r') as text_file:
        content = text_file.read()
    return content


def main():
    text_from_file = get_file_content()


if __name__ == '__main__':
    main()