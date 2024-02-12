from functools import reduce

puzzle_input = [[52, 426], [94, 1374], [75, 1279], [94, 1216]]


def part_one(races):
    result = 1
    for race in races:
        time = race[0]
        record = race[1]
        min_time = time
        for i in range(1, time):
            if (time - i) * i > record:
                min_time = i
                break
        max_time = min_time
        for i in reversed(range(min_time, time - 1)):
            if (time - i) * i > record:
                max_time = i
                break
        result *= ((max_time - min_time) + 1)
    return result


def part_two(races):
    tmp = [list(
        map(lambda x: int(x), reduce(lambda a, b: [str(a[0]) + '' + str(b[0]), str(a[1]) + '' + str(b[1])], races)))]
    return part_one(tmp)


print(part_one(puzzle_input))
print(part_two(puzzle_input))
