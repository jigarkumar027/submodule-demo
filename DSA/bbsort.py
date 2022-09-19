a = [55,66,2,3,1,0,9]

def bbsort(array):
    for ele in range(len(array)):
        for cele in range(ele,len(array)):
            if array[ele] > array[cele]:
                array[ele],array[cele] = array[cele],array[ele]
    return array

print(bbsort(a))

