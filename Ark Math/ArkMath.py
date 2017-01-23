class Matrix:
    def __init__(self, data):
        self.data = data
    def __getitem__(self, index):
        return self.data[index]
    def size(self):
        temp = [len(self.data)]
        tempAtIndex = self.data[0]
        while True:
            if type(tempAtIndex) == list:
                temp.append(len(tempAtIndex))
                tempAtIndex = tempAtIndex[0]
            else:
                break
        return temp
    def __len__(self):
        return len(self.data)
    def __str__(self):
        def _R(inp):
            if len(inp) > 0:
                if type(inp[0]) != list:
                    return "["+", ".join([str(i) for i in inp])+"]"
                else:
                    return "[" + ", ".join([_R(i) for i in inp]) + "]"
            else:
                return "[]"
        return _R(self.data)
    def __add__(self, toAdd):
        if self.size() != toAdd.size():
            return Matrix([])
        else:
            temp = []
            return temp
            
A = Matrix([[1, 2],[3, 4]])

print A.size()