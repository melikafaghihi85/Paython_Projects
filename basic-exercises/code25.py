import time

def timer(func):
    def wrapper(n):
        start = time.time()         
        result = func(n)            
        end = time.time()           

        print(result)
        print(f"Execution Time: {end - start:.6f} seconds")

        return result
    return wrapper

@timer
def create_list(n):
    return list(range(1, n + 1))


n = int(input())


create_list(n)