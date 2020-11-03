# we cannot modify tuples
# tuples are immutable
# for defining a tuple we will use paranthesis
# we can use tuples in our applications as a static list (not changing)

def execute_tuples():
    numbers = (1, 2, 3)
    print(numbers[0])


def unpacking_tuple():
    numbers = (4, 5, 6)

    # this is same as following
    # x = numbers[0]
    # y = numbers[1]
    # z = numbers[2]
    x, y, z = numbers
    print(f"{x}, {y}, {z}")
    print(x * y * z)


def unpacking_list():
    numbers = [7, 8, 9]

    # this is same as following
    # x = numbers[0]
    # y = numbers[1]
    # z = numbers[2]
    x, y, z = numbers
    print(f"{x}, {y}, {z}")
    print(x * y * z)


if __name__ == '__main__':
    # execute_tuples()
    # unpacking_tuple()
    unpacking_list()
