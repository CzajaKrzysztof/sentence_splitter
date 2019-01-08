def get_file_content(filename='text.txt'):
    """ Reads content of given text file and return it as string. """
    with open(filename, 'r') as text_file:
        content = text_file.read()
    return content


def get_position_to_check(text_from_file, index_list): 
    try:
        question_index = text_from_file.index('?')
    except ValueError:
        print("There are no ? in given text.")
        question_index = None

    try:
        exclamation_index = text_from_file.index('!')
    except ValueError:
        print("There are no ! in given text.")
        exclamation_index = None

    dot_index = text_from_file.index('.')
    if dot_index in index_list:
        dot_index = text_from_file[index_list[-1] + 1:].index('.') + index_list[-1]

    print("? {0}, ! {1}, . {2}".format(question_index, exclamation_index, dot_index))
    index = dot_index
    if question_index is not None:
        if question_index < index:
            index = question_index
    if exclamation_index is not None:
        if exclamation_index < index:
            index = exclamation_index
    print("index_list: {0}".format(index_list))             # TODO: delete
    return index


def get_char_at_index(text_from_file, index):
    char_at_index = text_from_file[index]
    return char_at_index


def get_sample_slice(text_from_file, index):
    # TODO: ma wyciagnac z tekstu wycinek z '.' 2 znaki za '.' i 3 znaki przed '.'
    # return slice_sample
    pass


def check_slice_with_dot(sample_slice):
    # TODO: ma psrawdzic kilka warunku podzialu linikej dla '.'
    # return result
    pass


def extract_sentence(text_from_file, position_to_check, sentence_list):
    # TODO: ma wyciagnac zdanie z tekstu i dodac go do sentenct_list.
    # return sentence_list
    pass


def main():
    sentence_list = []
    index_list = []
    text_from_file = get_file_content()
    position_to_check = get_position_to_check(text_from_file, index_list)
    print(position_to_check)                                                            # TODO: delete
    char_at_index = get_char_at_index(text_from_file, position_to_check)
    print(char_at_index)                                                                # TODO: delete
    # if char_at_index == '?':
    #     extract_sentence(text_from_file, position_to_check, sentence_list)
    #     sentence_list = []
    #     text_from_file = text_from_file[position_to_check + 1:]
    # elif char_at_index == '!':
    #     extract_sentence(text_from_file, position_to_check, sentence_list)
    #     sentence_list = []
    #     text_from_file = text_from_file[position_to_check + 1:]
    # elif char_at_index == '.':
    #     sample_slice = get_sample_slice(text_from_file, position_to_check)
    #     check_result = check_slice_with_dot(sample_slice)
    #     if check_result is True:
    #         extract_sentence(text_from_file, position_to_check, sentence_list)
    #         sentence_list = []
    #         text_from_file = text_from_file[position_to_check + 1:]
    #     else:
    #         index_list.append(position_to_check)


if __name__ == '__main__':
    main()
