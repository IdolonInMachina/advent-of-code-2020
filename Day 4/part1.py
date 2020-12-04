
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
            counter += 1
        else:
            print(passport)
    return counter


if __name__ == '__main__':
    data = load_input()
    print(len(data))
    answer = calculate(data)
    print(answer)
