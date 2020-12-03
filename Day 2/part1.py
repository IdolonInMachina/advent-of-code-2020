import re


def is_valid_password(minimum, maximum, character, password):
    counter = 0
    for char in password:
        if char == character:
            counter += 1
    return minimum <= counter <= maximum


if __name__ == '__main__':
    with open('input.txt') as f:
        data = f.readlines()
    counter = 0
    regex = r'([0-9]*)\-([0-9]*) ([a-z]): ([a-z]*)'
    for line in data:
        m = re.search(regex, line)
        minimum = m.group(1)
        maximum = m.group(2)
        char = m.group(3)
        password = m.group(4)
        if (is_valid_password(int(minimum), int(maximum), char, password)):
            counter += 1
    print(f"There are {counter} valid passwords")
