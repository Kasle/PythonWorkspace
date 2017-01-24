import brainfucki as bf
import random

#11, 6, 5

inp = "abcdefghijklmnopqrstuvwxyz"

print("Approx Max:", len(inp)*5000)

options = list("><+-.[]")

currGen = ["".join([random.choice(options) for i in range(random.randint(10, 100))]) for j in range(1000)]
nextGen = []

while True:
    nextGen = []
    currGen += ["".join([random.choice(options) for i in range(random.randint(1, 100))]) for j in range(100)]
    while len(currGen):
        code = currGen.pop(0)
        out = bf.bfrun(code, len(inp))[0]

        fitness = 0

        #print (code, len(out), len(inp))

        fitness += len(code)
        fitness += 2*abs(len(inp) - len(out))
        for i in range(min(len(inp),len(out))):
            fitness += abs(ord(inp[i])-ord(out[i]))

        fitness*=-1
        
        if len(nextGen) > 0:
            for i in range(len(nextGen)):
                if nextGen[i][1] < fitness:
                    nextGen.insert(i, [code, fitness])
                    break
            nextGen.append([code, fitness])
        else:
            nextGen.append([code, fitness])

    nextGen = nextGen[:10]
    currGen = []

    print ( nextGen[0][0] )
    #print (nextGen[0], bf.bfrun(nextGen[0], len(inp)))

    for node in range(len(nextGen)):
        currGen.append(nextGen[node][0])
        for count in range(20):

            temp = ""
            
            for index in range(len(nextGen[node][0])):
                val = random.random()
                if val < 0.2:
                    continue
                elif val < 0.2:
                    temp+=random.choice(options)
                else:
                    temp+=nextGen[node][0][index]

            if random.random() < 0.6:
                temp+="".join([random.choice(options) for radd in range(random.randint(0, 5))])
            
            currGen.append(temp)
