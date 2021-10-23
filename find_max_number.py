def find_max_number(numbers):
    max_number = None

    for number in numbers:
        if max_number is None or number > max_number:
            max_number = number

    return max_number


def main():
    numbers = [2, 3, 4, 5, 6, 7]
    max_number = find_max_number(numbers)
    print(max_number)


main()
