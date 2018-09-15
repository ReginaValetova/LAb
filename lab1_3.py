import math

str = input()
massif = str.split(',')

for i in range(0, len(massif)):
    massif[i] = int(massif[i])

# Bubble sort 

def bubble_sort(arr):
    n = 1

    while n < len(arr):
        for i in range(len(arr) - n):
            if arr[i] > arr[i + 1]:
                arr[i],arr[i+1] = arr[i+1],arr[i]
        n += 1
    return arr


#Gnome sort

def gnome_sort(arr):
    i = 1

    while i < len(arr):
        if arr[i - 1] <= arr[i]:
            i+=1
        else:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
            i-=1
    return arr

#Bucket sort

def bucket_sort(arr, bucketSize=3, ascending=True):
    
    if len(arr) == 0:
        return arr

    # Determine minimum and maximum values
    minValue = arr[0]
    maxValue = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < minValue:
            minValue = arr[i]
        elif arr[i] > maxValue:
            maxValue = arr[i]

    # Initialize buckets
    bucketCount = math.floor((maxValue - minValue) / bucketSize) + 1
    buckets = []
    for i in range(0, bucketCount):
        buckets.append([])

    # Distribute input array values into buckets
    for i in range(0, len(arr)):
        buckets[math.floor((arr[i] - minValue) / bucketSize)].append(arr[i])

    # Sort buckets and place back into input array
    arr = []
    for i in range(0, len(buckets)):
        buckets[i] = bubble_sort(buckets[i])
        for j in range(0, len(buckets[i])):
            arr.append(buckets[i][j])
    return arr

#Heapsort

def swap(i, j, arr):                    
    arr[i], arr[j] = arr[j], arr[i] 

def heapify(end,i, arr):   
    l=2 * i + 1  
    r=2 * (i + 1)   
    max = i   
    if l < end and arr[i] < arr[l]:   
        max = l   
    if r < end and arr[max] < arr[r]:   
        max = r   
    if max != i:   
        swap(i, max, arr)   
        heapify(end, max, arr)  
     
def heap_sort(arr):     
    end = len(arr)   
    start = end // 2 - 1 # use // instead of /
    for i in range(start, -1, -1):   
        heapify(end, i, arr)   
    for i in range(end-1, 0, -1):   
        swap(i, 0, arr)   
        heapify(i, 0, arr) 
    return arr  


print('\n')
print('Метод сортировки - пузырьковый:')
print(bubble_sort(massif)) 
print('\n')
print('Метод сортировки - гномий:')
print(gnome_sort(massif))
print('\n')
print('Метод сортировки - пирамидальный:')
print(heap_sort(massif))
print('\n')
print('Метод сортировки - блочный:')
print(bucket_sort(massif))
print('\n')


