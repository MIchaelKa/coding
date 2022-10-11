from __future__ import annotations

def binary_search(nums: list[int], target: int) -> int:
    
    low = 0
    high = len(nums) - 1
    
    while low <= high :
        mid = int((low + high) / 2)
        guess = nums[mid]
        if guess == target:
            return mid
        elif guess < target:
            low = mid + 1
        else:
            high = mid - 1
            
    return None