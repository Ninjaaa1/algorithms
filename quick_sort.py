from random import randint
def quick_sort(arr):
    if len(arr) < 2: # base case
        return arr
    else: # recursion case
        pivot = arr[0]
        less = [i for i in arr[1:] if i < pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)
print(quick_sort([randint(0, 3000) for x in range(30)])) # You can sort other numbers, if you want.