list=[20, 40, 34, 23, 89, 15, 2, 100, 25, 30]
array = int(input("Masukkan Angka Yang Di Cari: "))

def bubbleSort(list):
    for Number in range(len(list)-1,0,-1):
        for i in range(Number):
            if list[i]>list[i+1]:
                temp = list[i]
                list[i] = list[i+1]
                list[i+1] = temp
bubbleSort(list)
print("Sesudah Di Sorting", list)

def binarySearch(array, num_find):
    start = 0
    end = len(list) - 1
    mid = (start + end)//2
    found = False
    position = -1
    while start <= end:
        if list[mid] == num_find:
            found = True
            position = mid
            break
        if num_find > list[mid]:
            start = mid + 1
            mid = (start + end)//2
        else:
            end = mid - 1
            mid = (start + end)//2
    return (found, position-1)

num = array
found = binarySearch(array, num)
if found[0]:
    print('Elemen %d ditemukan pada posisi ke %d'%(num, found[1]+2))
else:
    print('Elemen %d tidak ditemukan t'%num)
