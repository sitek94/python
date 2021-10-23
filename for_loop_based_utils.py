my_numbers = [1, 2, 3, 10, 4, 21, 7, 2, 13, 3]


def sum(numbers):
    total = 0
    for n in numbers:
        total += n
    return total


print('Sum:', sum(my_numbers))


def length(numbers):
    count = 0
    for n in numbers:
        count += 1
    return count


print('Length:', length(my_numbers))


def average(numbers):
    total = sum(numbers)
    count = length(numbers)
    return total / count


print('Average:', average(my_numbers))


def greater_than(numbers, max):
    new_numbers = []
    for n in numbers:
        if n > max:
            new_numbers.append(n)
    return new_numbers


print('Greater than 5:', greater_than(my_numbers, 5))
