# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 08:20:53 2020

@author: Long Mai
"""

def read_file(file_name): # read a file file_name and return the list of numbers
    nums = list()
    with open(file_name) as file:
        for line in file:
            line = line.strip()
            nums.append(int(line))
    return nums
nums_list = read_file("IntegerArray.txt")
def count_inversion(nums):
    # return the number of inversions in the list nums
    def count_and_merge(start, stop):
        
        # trivial case
        if start >= stop:
            return 0
        
        # count the number of inversions from the first list, the second list, and the mix
        mid = (start + stop)//2
        count_left = count_and_merge(start, mid)
        count_right = count_and_merge(mid + 1, stop)
        count_mix = 0
        right = mid + 1
        for left in range(start, mid + 1):
            while right <= stop and nums[right] < nums[left]:
                right += 1
            count_mix += right - (mid + 1)
        
        # do the merge sort
        new_list = list()
        i = start 
        j = mid + 1
        while i <= mid and j <= stop:
            if nums[i] < nums[j]:
                new_list.append(nums[i])
                i += 1
            else:
                new_list.append(nums[j])
                j += 1
        if i == mid + 1:
            while j <= stop:
                new_list.append(nums[j])
                j += 1
        else:
            while i <= mid:
                new_list.append(nums[i])
                i += 1
        count_new_list = 0
        for i in range(start, stop + 1):
            nums[i] = new_list[count_new_list]
            count_new_list += 1
            
        return count_left + count_right + count_mix
    return count_and_merge(0, len(nums) - 1) 

count = count_inversion(nums_list)
print(count)