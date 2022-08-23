nums = [8,9,15,22,7,11,12,3] # You can type your own numbers here.

def sum_nums(arr):
    if arr == []: # base case v1
        return 0
    elif len(arr) == 1: # base case v2
        return arr[0]
    else: # recursion case
        return arr[0] + sum_nums(arr[1:len(arr)]) 
    

print(sum_nums(nums))