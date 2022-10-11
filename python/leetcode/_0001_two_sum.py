from typing import List
from common.utils import binary_search

def twoSum_brute(nums: List[int], target: int) -> List[int]:    
    for i in range(len(nums)):            
        num = nums[i]
        for j in range(i+1, len(nums)):
            num_2 = nums[j]
            if num + num_2 == target:
                return [i,j]

def twoSum_v1(nums: List[int], target: int) -> List[int]:
    
    indexes = sorted(range(len(nums)), key=lambda k: nums[k])
    
    nums_s = sorted(nums)
    nums_s = nums[indexes]

    for i in range(len(nums_s)-1):            
        num = nums_s[i]
        num_2 = target - num
        
        nums_to_search = nums_s[i+1:]    
        j = binary_search(nums_to_search, num_2)        
        if j is not None:
            return [indexes[i], indexes[j+i+1]]

def twoSum_v2(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)-1):            
        num = nums[i]
        num_2 = target - num
        
        nums_to_search = nums[i+1:]
        if num_2 in nums_to_search:
            j = nums_to_search.index(num_2)
            return [i, j+i+1]

def twoSum_v3(nums: List[int], target: int) -> List[int]:
    hashmap = {}
    for i, v in enumerate(nums):
        hashmap[v] = i
    for i, v in enumerate(nums):
        num = target - v
        if num in hashmap and num != v:
            return [i, dict[num]]

def twoSum_v4(nums: List[int], target: int) -> List[int]:  
    hashmap = {}
    for i, v in enumerate(nums):    
        num = target - v       
        if num in hashmap and hashmap[num] != i:
            return [i, hashmap[num]]        
        hashmap[v] = i