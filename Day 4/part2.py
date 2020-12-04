
def load_input():
    with open('input.txt', 'r') as f:
        data = f.readlines()
    result = []
    current = {}
    for line in data:
        if (line == '\n'):
            if (len(current) > 0):
                result.append(current)
            current = {}
        else:
            split = line.split(' ')
            for pair in split:
                split_again = pair.split(':')
                current[split_again[0]] = split_again[1]
    return result


def calculate(data):
    FIELDS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
    ACCEPTABLE_TO_MISS = ['cid']
    counter = 0
    for passport in data:
        valid = False
        matched = []
        unmatched = []
        for field in FIELDS:
            try:
                passport[field]
                if (field not in matched):
                    matched.append(field)
            except KeyError:
                unmatched.append(field)
        if (len(matched) == len(FIELDS)):
            valid = True
        else:
            all_acceptable = True
            for missing in unmatched:
                if missing not in ACCEPTABLE_TO_MISS:
                    all_acceptable = False
                    break
            if (all_acceptable):
                valid = True
        if (valid):
            all_valid = True
            for field in passport:
                valid_field = validate_field(field, passport[field])
                if not valid_field:
                    all_valid = False
            if (all_valid):
                counter += 1
    return counter


def validate_field(key, value):
    valid = False
    if value[-1] == '\n':
        value = value[:-1]
    if (key == 'byr'):
        valid = number_in_bounds(value, 1920, 2002)
    elif (key == 'iyr'):
        valid = number_in_bounds(value, 2010, 2020)
    elif (key == 'eyr'):
        valid = number_in_bounds(value, 2020, 2030)
    elif (key == 'hgt'):
        if (value[-2:] == 'in'):
            value = value[:-2]
            valid = number_in_bounds(value, 59, 76)
        elif (value[-2:] == 'cm'):
            value = value[:-2]
            valid = number_in_bounds(value, 150, 193)
    elif (key == 'hcl'):
        valid_here = True
        if (value[0] != '#'):
            valid_here = False
        value = value[1:]
        if (len(value) != 6):
            valid_here = False
        try:
            int(value, 16)
        except ValueError:
            valid_here = False
        if (valid_here):
            valid = True
    elif (key == 'ecl'):
        VALID_CHOICES = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        if (value in VALID_CHOICES):
            valid = True
    elif (key == 'pid'):
        valid_here = True
        if (len(value) != 9):
            valid_here = False
        try:
            int(value)
        except ValueError:
            valid_here = False
        if (valid_here):
            valid = True
    elif (key == 'cid'):
        valid = True
    else:
        valid = False
    return valid


def number_in_bounds(value, minimum, maximum):
    try:
        value = int(value)
    except ValueError:
        return False
    return (minimum <= value <= maximum)


if __name__ == '__main__':
    data = load_input()
    answer = calculate(data)
    print(answer)
