'''
topk by quick sort
assert: k <= len(arr)
'''
def topkByQuickSort(k,arr=None):
   topk=[]
   return quickSort(0,len(arr)-1,k,topk,arr)

'''
quick sort to find top k for an unsorted array
'''
def quickSort(lo,hi,k,topk,arr):
    # this is worst condition for topk
    if lo>=hi:
        index = len(arr) - k
        while index < len(arr):
            topk.append(arr[index])
            index+=1
        return topk
    #following basic quick sort idea
    i = lo
    j = hi
    pivot = arr[lo]
    while i < j:
        while j > i and pivot <= arr[j]:
            j-=1
        arr[i] = arr[j]
        while i < j and arr[i] < pivot:
            i+=1
        arr[j] = arr[i]
    #put pivot to i index
    arr[i] = pivot
    # following is important, if i less than length of array minus k, then iterator to high part;
    # elif bigger, then iterator to low part
    # else equal, get it!
    if i < len(arr) - k :
        quickSort(i+1,hi,k,topk,arr)
    elif i > len(arr) - k:
        quickSort(lo,i-1,k,topk,arr)
    else:
        index = i
        while index < len(arr):
            topk.append(arr[index])
            index+=1
    return topk
	
	
topk = topkByQuickSort(1,arr=[3,5,1,6,9,8,5,12])
[print(item) for item in topk]
12


topk = topkByQuickSort(2,arr=[3,5,1,6,9,8,5,12])
[print(item) for item in topk]
9
12


topk = topkByQuickSort(8,arr=[32,5,7,6,13,9,8,4,12])
[print(item) for item in topk]
5
7
6
8
9
12
13
32