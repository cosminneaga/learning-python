def highest_even(collection):
    evens = []
    for item in collection:
        if item % 2 == 0:
            evens.append(item)

    largest_number = 0
    for item in evens:
        for x in evens:
            if item > x and item > largest_number:
                largest_number = item

    return largest_number


print(highest_even([10, 2, 3, 1000, 4, 8, 11, 20, 21, 100]))


def highest_even(collection):
    evens = []
    for item in collection:
        if item % 2 == 0:
            evens.append(item)

    return max(evens)


print(highest_even([10, 2, 3, 1000, 4, 8, 11, 20, 21, 100]))
