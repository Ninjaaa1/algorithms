unsorted_list = [6,3,1,7,9,11,4,15,99,12,199,2,-1] # You can type your own list here, which you want to sort. 

def findSmallest(arr): # Function to find the smallest number from a list.
    smallest = arr[0] # The smallest number, but for the first time, PC don't know, which number is the smallest.
    smallest_index = 0
    for i in range(1, len(arr)): # Finding the smallest number and overwrite "smallest" variable.
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selection_sort(list_to_sort):
    new_list = list()
    for i in range(len(list_to_sort)):
        smallest = findSmallest(list_to_sort)
        new_list.append(list_to_sort.pop(smallest)) # Adding number from old list to new and deleting from old lsit.
    return new_list

print(selection_sort(unsorted_list))
