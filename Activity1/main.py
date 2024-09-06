#Bubble Sort - Asc
array1 = [23, 89, 7, 56, 44]
print("Array:")
print(array1)
for i in range(len(array1)):
    for j in range(0, len(array1) - i - 1):
        if array1[j] > array1[j + 1]:
            array1[j], array1[j + 1] = array1[j + 1], array1[j]
print("Array after bubble sort in ascending order:")
print(array1)

print()

#Insertion Sort - Asc
array2 = [12, 78, 91, 34, 62]
print("Array:")
print(array2)
for i in range(1, len(array2)):
    key = array2[i]
    j = i - 1
    while j >= 0 and key < array2[j]:
        array2[j + 1] = array2[j]
        j -= 1
    array2[j + 1] = key
print("Array after insertion sort in ascending order:")
print(array2)

print()

#Selection Sort - Desc
array3 = [5, 99, 48, 15, 67]
print("Array:")
print(array3)
for i in range(len(array3)):
    min_idx = i
    for j in range(i + 1, len(array3)):
        if array3[min_idx] > array3[j]:
            min_idx = j
    array3[i], array3[min_idx] = array3[min_idx], array3[i]
print("Array after selection sort in descending order:")
print(array3)

print()

#Insertion Sort - Desc
array4 = [38, 82, 25, 74, 13]
print("Array:")
print(array4)
for i in range(1, len(array4)):
    key = array4[i]
    j = i - 1
    while j >= 0 and key > array4[j]:
        array4[j + 1] = array4[j]
        j -= 1
    array4[j + 1] = key
print("Array after insertion sort in descending order:")
print(array4)

print()

#Selection Sort - Asc and Bubble Sort - Desc
array5 = [24, 44, 34, 62, 15, 48, 74, 38]
array6 = array5
print("Array:")
print(array5)
for i in range(len(array6)):
    min_idx = i
    for j in range(i + 1, len(array6)):
        if array6[min_idx] > array6[j]:
            min_idx = j
    array6[i], array6[min_idx] = array6[min_idx], array6[i]
print("Array after selection sort in ascending order:")
print(array6)

print()

array7 = array5
print("Array:")
print(array5)
for i in range(len(array7)):
    for j in range(0, len(array7) - i - 1):
        if array7[j] < array7[j + 1]:
            array7[j], array7[j + 1] = array7[j + 1], array7[j]
print("Array after bubble sort in descending order:")
print(array7)

print()

array8 = [7, 23, 44, 56, 89, 12, 34, 62, 78, 91, 5, 15, 48, 67, 99, 82, 74, 38, 25, 13]
print("Array:")
print(array8)
for i in range(len(array8)):
    min_idx = i
    for j in range(i + 1, len(array8)):
        if array8[min_idx] > array8[j]:
            min_idx = j
    array8[i], array8[min_idx] = array8[min_idx], array8[i]
print("Array after selection sort in ascending order:")
print(array8)

print()

even = []
odd = []
for num in range(len(array8)):
    if num % 2 == 0:
        even.append(num)
    if num % 2 != 0:
        odd.append(num)

print("Array of even numbers:")
print(even)
print("Array of odd numbers:")
print(odd)