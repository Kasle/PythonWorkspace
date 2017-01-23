import brainfucki as bf
import random

#11, 6, 5

options = list("><+-.[]")

pool = ["".join([random.choice(options) for i in range(random.randint(1, 20))]) for j in range(100)]
tempPool = []

while True:
    for i in pool:
        score = 0
        output = bf.bfrun(i, 20)
        score+=len(output[0])
        if not output[2]:
            score = 0
        if score != 0:
            tempPool.append(i)
        #print(score, i)

    print (tempPool)
    break


