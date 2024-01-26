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


#
# Recursive attempt to implement binary_search
#
def quick_search(nums: list[int], target: int) -> int:

    nums_len = len(nums)
    
    if nums_len == 0:
        return None
   
    i = int(nums_len / 2)

    if (nums[i] == target):
        return i
    elif nums[i] < target:
        # print("L", nums[i+1:])
        return quick_search(nums[i+1:], target)
    else:
        # print("R", nums[:i-1])
        return quick_search(nums[:i], target)
    
def print_cost_matrix(matrix: list[list[int]]) -> None:
    for i in range(len(matrix)):
        print("[", end="")
        for j in range(len(matrix[i])):
            print(f"{matrix[i][j]:3d}", end="")
        print("]")