# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 16:33:03 2017

@author: ice-fire
"""

def partition(nums):
    answer = 0
    i, j = 0, len(nums) - 1
    while i < j:
        if nums[i] == 1 and nums[j] == 0:
            nums[i], nums[j] = nums[j], nums[i]
            answer += 1
            i += 1
            j -= 1
        else:
            if nums[i] == 0:
                i += 1
            if nums[j] == 1:
                j -=1
        
    print(nums)
    print("交换的次数：", answer)
    return answer

nums = [1,0,1,0,0,1,1,0,1,0,1,0,1,0,0,1]
partition(nums)     
        
