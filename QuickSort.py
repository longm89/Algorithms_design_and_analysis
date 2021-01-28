# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 08:02:30 2021

@author: Long Mai
"""

def read_file(file_name): # read a file file_name and return the list of numbers
    nums = list()
    with open(file_name) as file:
        for line in file:
            line = line.strip()
            nums.append(int(line))
    return nums
nums_list = read_file("QuickSort.txt")
def QuickSort(a, left, right):
    if right - left + 1 <= 1:
        return 0
    
    def ChoosePivot(a, left, right):
        median = 0 
        if (right - left + 1) % 2 == 0:
            median = left + (right - left + 1)//2 - 1 
        else:
            median = left + (right - left + 1)//2
        if (a[left] <= a[median]) and (a[median] <= a[right]):
            return median
        if (a[left] <= a[right]) and (a[right] <= a[median]):
            return right
        if (a[right] <= a[median]) and (a[median] <= a[left]):
            return median
        if (a[right] <= a[left]) and (a[left] <= a[median]):
            return left
        if (a[median] <= a[left]) and (a[left] <= a[right]):
            return left
        if (a[median] <= a[right]) and (a[right] <= a[left]):
            return right
    total = 0
    total += right - left 
    p = ChoosePivot(a, left, right)
    
    a[left], a[p] = a[p], a[left]

    i = left + 1
    for j in range(left + 1, right + 1):
        if a[j] < a[left]:
            a[j], a[i] = a[i], a[j]
            i += 1
    a[left], a[i-1] = a[i - 1], a[left]

    total += QuickSort(a, left, i - 2)
    total += QuickSort(a, i, right)
    return total

print(QuickSort(nums_list, 0, len(nums_list) - 1))
