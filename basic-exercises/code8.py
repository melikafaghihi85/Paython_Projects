x = 55000
if x > 50000 :
    discount = 0.20 
    final = x * (1-discount)
    print (final)
elif 20000 <= x <= 50000 :
    discount = 0.10 
    final = x * (1-discount)
    print (final)
elif x < 20000 : 
    print (x)