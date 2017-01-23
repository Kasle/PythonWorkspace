import time
toSort = [1, 5, 2, -7, 4, 9, 2, 0]
import random

print "-max"

for x in range(5):
    st = time.time()
    for i in range(1000000):
        x = [random.randint(-100, 100), random.randint(-100, 100)]
        b = max(x)
    print time.time() - st

print "-min"

for x in range(5):
    st = time.time()
    for i in range(1000000):
        x = [random.randint(-100, 100), random.randint(-100, 100)]
        b = min(x)
    print time.time() - st

print "-selfmax"

for x in range(5):
    st = time.time()
    for i in range(1000000):
        x = [random.randint(-100, 100), random.randint(-100, 100)]
        b = x[int(x[0] < x[1])]
    print time.time() - st

print "-selfminx"

for x in range(5):
    st = time.time()
    for i in range(1000000):
        x = [random.randint(-100, 100), random.randint(-100, 100)]
        b = x[int(x[0] > x[1])]
    print time.time() - st
