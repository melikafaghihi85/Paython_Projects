def pick_evens(*args):
    result = []
    for i in args:
        if i % 2 == 0:
            result.append(i)
    return result
r = pick_evens(1, 2, 3, 4, 5, 6)
print(r)
r_2 = pick_evens(7, 13, 19, 21)
print(r_2)