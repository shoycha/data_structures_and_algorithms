"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def quicksort(array):
    quicksorthelper(array, 0, len(array)-1)
    
def quicksorthelper(array, low, high):

    if low < high:
        partition = get_partition(array, low, high)
        quicksorthelper(array, low, partition - 1)
        quicksorthelper(array, partition+1, high)

def get_partition(array, low, high):
    
    done = False
    partition = array[high]
    current_partition_index = high
    leftside = low
    rightside = high - 1
    while not done:
        if array[leftside] >= partition:
            array[leftside], array[rightside] = array[rightside], array[leftside]
            array[rightside], array[current_partition_index] = array[current_partition_index],array[rightside]
            current_partition_index -= 1
            rightside -= 1
        if array[leftside] < partition:
            leftside += 1
        if leftside > rightside:
            done = True
    return current_partition_index
        
    

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
quicksort(test)
print(test)
alist = [54,26,93,17,77,31,44,55,20]
quicksort(alist)
print(alist)
test = [1]
quicksort(test)
print(test)
test = [3,2,1]
quicksort(test)
print(test)
