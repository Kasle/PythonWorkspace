import brainfucki as bf
import random

#11, 6, 5

inp = "12345"

print("Approx Max:", len(inp)*5000)

options = list("><+-.[]")

currGen = ["".join([random.choice(options) for i in range(random.randint(10, 100))]) for j in range(1000)]
nextGen = []

while True:
    currGen += ["".join([random.choice(options) for i in range(random.randint(1, 100))]) for j in range(50)]
    while len(currGen):
        code = currGen.pop(0)
        out = bf.bfrun(code, len(inp))[0]

        fitness = 0

        for i in range(max(len(inp), len(out))):
            if i >= len(out):
                fitness += -ord(inp[i])
            elif i < len(out) and i < len(inp):
                fitness += 100*(1000.0 / (1+abs(ord(inp[i])-ord(out[i]))))
            elif i >= len(inp):
                fitness += -ord(out[i])
            else:
                print('err')

        fitness -= len(code)*100

        if len(nextGen) > 0:
            for i in range(len(nextGen)):
                if nextGen[i][1] < fitness:
                    nextGen.insert(i, [code, fitness])
                    break
            nextGen.append([code, fitness])
        else:
            nextGen.append([code, fitness])

    nextGen = nextGen[:5]

    print (nextGen[0])

    for A in range(len(nextGen)-1):
        for B in range(A+1, len(nextGen)):
            temp = ""
            
            for index in range(max(len(nextGen[A][0]),len(nextGen[B][0]))):
                if random.random() < 0.1:
                    continue
                
                if random.random() < 0.2:
                    temp+=random.choice(options)
                
                if random.random() < 0.2:
                    temp+=random.choice(options)
                elif index < len(nextGen[A][0]) and index < len(nextGen[B][0]):
                    if random.random() < 0.5:
                        temp+=nextGen[A][0][index]
                    else:
                        temp+=nextGen[B][0][index]
                elif index < len(nextGen[A][0]):
                    temp+=nextGen[A][0][index]
                else:
                    temp+=nextGen[B][0][index]

            if random.random() < 0.6:
                temp+="".join([random.choice(options) for radd in range(random.randint(0, 5))])
            
            currGen.append(temp)
