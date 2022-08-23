our_array = [1, "jabłko", 3, "ser"] # You can type your own array here.

def length_of_the_array(arr):
    if arr is None or arr == []: # base cese
        return 0
    else: # recursion case
        return 1 + length_of_the_array(arr[1::2]) + length_of_the_array(arr[2::2]) # sum( 1, odd and even numbers)

print(length_of_the_array(our_array))