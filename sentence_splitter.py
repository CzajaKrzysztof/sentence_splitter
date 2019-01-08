import titles


def get_file_content(filename='text.txt'):
    """ Reads content of given text file and return it as string. """
    with open(filename, 'r') as text_file:
        content = text_file.read()
    return content


def get_position_to_check(text_from_file, index_list):
    try:
        question_index = text_from_file.index('?')
    except ValueError:
        question_index = None

    try:
        exclamation_index = text_from_file.index('!')
    except ValueError:
        exclamation_index = None

    dot_index = text_from_file.index('.')
    if dot_index in index_list:
        dot_index = text_from_file[index_list[-1] + 1:].index('.') + index_list[-1] + 1

    index = dot_index
    if question_index is not None:
        if question_index < index:
            index = question_index
    if exclamation_index is not None:
        if exclamation_index < index:
            index = exclamation_index
    return index


def get_char_at_index(text_from_file, index):
    char_at_index = text_from_file[index]
    return char_at_index


def get_sample_slice(text_from_file, index):
    slice_begining = index - 3
    if slice_begining < 0:
        slice_begining = 0
    sample_slice = text_from_file[slice_begining:index + 3]

    return sample_slice


def get_dot_index(sample_slice):
    if len(sample_slice) == 5:
        dot_index = 2
    elif len(sample_slice) == 4:
        dot_index = 3
    else:
        dot_index = 3

    return dot_index


def check_slice_with_dot(sample_slice, titles_list):
    capital_letters = 'ABCDEFGHIJKLMNOPRSTUVWQXYZ'
    dot_index = get_dot_index(sample_slice)
    if dot_index == len(sample_slice) - 1:
        result = True
        return result

    if sample_slice[:dot_index] not in titles_list:
        if sample_slice[dot_index + 1] == ' ' and sample_slice[dot_index + 2] in capital_letters:
            result = True
        else:
            result = False
    else:
        result = False

    return result


def show_sentence_list(sentence_list):
    for i in sentence_list:
        print(i)


def main():
    sentence_list = []
    index_list = []
    titles_list = titles.titles.split(' ')
    text_from_file = get_file_content()
    while True:
        position_to_check = get_position_to_check(text_from_file, index_list)
        char_at_index = get_char_at_index(text_from_file, position_to_check)
        if char_at_index == '?':
            sentence_list.append(text_from_file[:position_to_check + 1].lstrip(' '))
            text_from_file = text_from_file[position_to_check + 1:]
            continue
        elif char_at_index == '!':
            sentence_list.append(text_from_file[:position_to_check + 1].lstrip(' '))
            text_from_file = text_from_file[position_to_check + 1:]
            continue
        elif char_at_index == '.':
            sample_slice = get_sample_slice(text_from_file, position_to_check)
            check_result = check_slice_with_dot(sample_slice, titles_list)
            if check_result is True:
                sentence_list.append(text_from_file[:position_to_check + 1].lstrip(' '))
                text_from_file = text_from_file[position_to_check + 1:]
                index_list = []
            else:
                index_list.append(position_to_check)

        if text_from_file == '':
            show_sentence_list(sentence_list)
            break


if __name__ == '__main__':
    main()
