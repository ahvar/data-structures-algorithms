from rich import print as rprint
def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selection_sort(arr):
    new_arr = []
    arr_copy = list(arr)
    for i in range(len(arr_copy)):
        smallest_index = find_smallest(arr_copy)
        new_arr.append(arr_copy.pop(smallest_index))
    return new_arr
    
if __name__ == "__main__":
    arr = [3,6,1,4,8,34,32,11,8,]
    rprint(selection_sort(arr))    