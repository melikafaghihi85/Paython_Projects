def zarb (*args):
    res = 1
    for i in args :
        res *= i
    return res
b = zarb(3, 4, 5, 6)
print (b)
