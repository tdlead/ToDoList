def get_todos(filename):
    """
    Read a text file and return the list of to-do items.

    This function opens a text file specified by `filename`, reads its contents line by line, and returns those lines as a list. Each line in the list represents a to-do item.

    :param filename: The name of the text file containing to-do items.
    :type filename: str
    :return: A list of strings, each representing a to-do item.
    :rtype: list
    """
    with open(filename, 'r') as file:
        data = file.readlines()
    return data


def write_file(filename, lines):
    """
    Write a list of strings to a text file.

    This function opens a text file specified by `filename` in write mode and writes each string from the `lines` list to the file. If the file already exists, it will be overwritten.

    :param filename: The name of the text file where the lines will be written.
    :type filename: str
    :param lines: A list of strings to be written to the file.
    :type lines: list
    """
    with open(filename, 'w') as file:
        file.writelines(lines)


def print_content(filename):
    """
    Read a text file and print its contents with line numbers.

    This function opens a text file specified by `filename`, reads its contents line by line, and prints each line prefixed with its line number. The line numbers start from 1.

    :param filename: The name of the text file to be read and printed.
    :type filename: str
    """
    with open(filename, 'r') as file:
        lines = file.readlines()
        for index, element in enumerate(lines):
            print(f'{index + 1} : {element.strip()}')


if __name__ == '__main__':
    print("Hello")
