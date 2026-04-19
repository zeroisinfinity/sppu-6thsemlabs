def selection_sort(arr : list , start : int , end : int):


    # SORT ARRAY FROM START TILL END INDEX

    for ele in range(start,end):
        
        # assume ele indx as smallest at each iteration
        min_idx = ele

        # greedily select idx of smallest ele and swap with min_idx
        for srt in range(ele,end):
            # if arr[srt] is lesser then update min_idx
            if arr[min_idx] > arr[srt]:
                min_idx = srt
        
        # swap
        arr[min_idx] , arr[ele] = arr[ele] , arr[min_idx]

    # return sorted array
    return arr

array1 = [45,8,23,99,44,0,-35,-66]
array1_sorted = selection_sort(array1,0,len(array1))
print(f'Sorted array is {array1_sorted}')
