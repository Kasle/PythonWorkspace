import random
alpha = [chr(i) for i in range(33, 127)]
print("".join(alpha))
passalpha = input("Enter modified alphanumeric string: ")
passlen = int(input("Enter desired password length: "))
for i in range(10):
    outpass = [passalpha[random.randint(0, len(alpha)-1)] for i in range(passlen)]
    print("".join(outpass))
