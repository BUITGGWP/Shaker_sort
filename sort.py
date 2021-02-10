def itc_shaker_sort(array): 
    length = len(array) 
    swapped = True
    start_index = 0
    end_index = length - 1
    while (swapped == True): 
        swapped = False
        for i in range(start_index, end_index):
            print(*array) 
            if (array[i] > array[i + 1]) : 
                array[i], array[i + 1] = array[i + 1], array[i] 
                swapped = True
        if (not(swapped)): 
            break
        swapped = False
        end_index = end_index - 1
        for i in range(end_index - 1, start_index - 1, -1):
            print(*array) 
            if (array[i] > array[i + 1]): 
                array[i], array[i + 1] = array[i + 1], array[i] 
                swapped = True
        start_index = start_index + 1
    return array


n = int(input())
print(*itc_shaker_sort(list(map(int, input().split()))))
