'''
maxheap
'''

#it uses the complated binary Tree to build it self 

def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]
        heapify(arr, n, largest)

def insert(array, newNum):
    size = len(array)
    if size == 0:
        array.append(newNum)
    else:
        array.append(newNum)
        for i in range((size//2)-1, -1, -1):
            heapify(array, size, i)

def checkheapy(array):
    size = len(array)
    for i in range(size,-1,-1):
        pass

arr = []
insert(arr,3)
insert(arr,6)
insert(arr,5)
insert(arr,55)
insert(arr,666) 
print('max-heap:',str(arr))