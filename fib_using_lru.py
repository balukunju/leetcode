from functools import lru_cache

@lru_cache(maxsize=1000)
def fib(n: int):
    if n <= 1:
        return 1
    return fib(n-1) + fib(n-2)

for i in range(0, 35):
    print (i,":",fib(i))
