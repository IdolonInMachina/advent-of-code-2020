
def load_input():
    input_map = []
    with open('input.txt', 'r') as f:
        input_data = f.readlines()
    for line in input_data:
        if (line[-1] == '\n'):
            line = line[:-1]
        input_map.append(line)
    return input_map


def calculate_path(input_map, x_increase, y_increase):
    x = 0
    y = 0
    counter = 0
    line_length = 0
    if len(input_map) > 0:
        line_length = len(input_map[0])
    while y < len(input_map):
        if input_map[y][x] == '#':
            counter += 1
        y += y_increase
        x += x_increase
        if (x >= line_length):
            x -= line_length
    return counter


if __name__ == '__main__':
    input_map = load_input()
    SLOPES = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    running_multiple = 1
    for slope in SLOPES:
        answer = calculate_path(input_map, slope[0], slope[1])
        running_multiple *= answer
    print(f"The number of trees hit across all slopes is {running_multiple}")
