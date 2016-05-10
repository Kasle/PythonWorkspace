def centered_average(nums):
    counter = 0
    index = [0, 0]
    min = nums[0]
    max = nums[0]
    for num in nums:
        if num > max:
            max = num
            index[0] = counter
        elif num < min:
            min = num
            index[1] = counter
        counter+=1
    reducedList = nums
    if index[0] < index[1]:
        del reducedList[index[0]]
        del reducedList[index[1]-1]
    else:
        del reducedList[index[1]]
        del reducedList[index[0]-1]

    avCount = 0
        
    for num in reducedList:
        avCount+=num

    avCount = avCount / len(reducedList)

    return avCount

print centered_average([1, 2, 12, 3, 7, 8, 2, 5])
