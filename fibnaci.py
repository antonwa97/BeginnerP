
import time

ts = time.time()
# fibonacci_cache = {}
#
# def fibonacci(n):
#     value = 0
#     if n in fibonacci_cache:
#         return fibonacci_cache[n]
#     elif n == 1:
#         value = 1
#     elif n == 2:
#         value = 1
#     elif n > 2:
#         value = fibonacci(n-1) + fibonacci(n-2)
#     fibonacci_cache[n] = value
#     return value
#
# a = 1000
# for n in range(1, a+1):
#     print(n, ':', fibonacci(n))
#
# dt = time.time()- ts
# print(dt)
from functools import lru_cache
@lru_cache(maxsize = 10000)


def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)
n = 10000
for n in range(n):
    print(n, ': ', fibonacci(n))

dt = time.time()- ts
print(dt)