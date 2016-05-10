current = open("CubeBlocks.sbc", "r")
lines = current.readlines()
for i in range(len(lines)):
    if "<BuildTimeSeconds>" in lines[i]:
        _si = lines[i].index(">")+1
        lines[i] = lines[i][:_si] + "0" + lines[i][lines[i].index("</"):]
current.close()

current = open("CubeBlocks.sbc", "w")
current.write("".join(lines))
current.close()

exit()
