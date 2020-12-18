"""
Counting Sort
This code works only with numerical dataset.
"""

def countingSort(array):
    __max = int(max(array)) 
    __min = int(min(array)) 
    __range = __max - __min + 1
    
    count = [0 for _ in range(__range)] 
    output = [0 for _ in range(len(array))] 

    for i in range(0, len(array)): 
        count[array[i] - __min] += 1

    for i in range(1, len(count)): 
        count[i] += count[i-1]

    for i in range(len(array)-1, -1, -1): 
        output[count[array[i] - __min] - 1] = array[i] 
        count[array[i] - __min] -= 1

    return output

dataset = list(map(int, input("Please enter dataset, by whitespace separated: ").split()))
print("Unsorted Data: ",dataset)
print("Sorted Data", countingSort(dataset))