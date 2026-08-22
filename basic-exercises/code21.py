def skyline(*args):
    if not args:
        return 0

    biggest = args[0]

    for i in args:
        if i > biggest:
            biggest = i

    return biggest


print(skyline(3, 7, 15, 2, 9))
print(skyline(1, 1, 1, 1))
