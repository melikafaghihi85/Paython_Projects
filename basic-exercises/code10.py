n = int(input())
if n < 2:
    print("عدد باید حداقل 2 باشد")
else:
    print(n)   
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        
        print(n)