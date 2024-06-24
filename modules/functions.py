def read_file(filename):
    with open(filename, 'r') as file:
        data = file.readlines()
    return data


def write_file(filename, lines):
    with open(filename, 'w') as file:
        file.writelines(lines)


def print_content(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        for index, element in enumerate(lines):
            print(f'{index + 1} : {element.strip()}')


if __name__ == '__main__':
    print("Hello")
