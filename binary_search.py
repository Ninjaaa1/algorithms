def binary_search(data, num):
    lowest = 0 
    highest = len(data) - 1 

    while lowest <= highest: 
        middle = (lowest + highest)//2 
        if num < data[middle]: 
            highest = middle 
        elif num > data[middle]: 
            lowest = middle + 1 
        else: 
            return middle 

    if lowest < len(data) and data[lowest] == num: 
        return lowest 

    return -1 
    
nums = [i for i in range(0,50)] # You can type your own numbers here.
numb = 30 # You can type your own number here.
print(binary_search(nums, numb)) 
