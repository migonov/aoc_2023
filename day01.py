def part_one():
    response = 0
    while True:
        line = input()
        if line == '':
            break
        first_digit = -1
        last_digit = -1
        for c in line:
            try:
                to_digit = int(c)
                if first_digit == -1:
                    first_digit = to_digit
                last_digit = to_digit
            except ValueError:
                pass
        response += first_digit * 10 + last_digit
    return response


valid_digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
digit_map = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}


def part_two():
    response = 0
    while True:
        line = input()
        if line == '':
            break
        first_digit = -1
        last_digit = -1
        for ind, c in enumerate(line):
            try:
                to_digit = int(c)
                if first_digit == -1:
                    first_digit = to_digit
                last_digit = to_digit
            except ValueError:
                for valid_digit in digit_map.keys():
                    if line.startswith(valid_digit, ind):
                        to_digit = digit_map[valid_digit]
                        if first_digit == -1:
                            first_digit = to_digit
                        last_digit = to_digit
                        break
        response += first_digit * 10 + last_digit
    return response


# print(part_one())
print(part_two())
