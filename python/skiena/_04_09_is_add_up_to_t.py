from __future__ import annotations
from common.utils import binary_search

def is_add_up_to_t(array: list[int], k: int, t: int) -> list[int]:
    array.sort()
    return is_add_up_to_t_helper(array, k ,t)
    

def is_add_up_to_t_helper(array: list[int], k: int, t: int) -> list[int]:
    """
    Solution 1.

    Complexity:
        time: O(n^(k-1)*log(n))
        memory: O(n^(k-1))
    """
    
    if k == 1:
        index = binary_search(array, t)
        if index is not None:
            return [array[index]]
        else:
            return None
    
    for i in range(len(array)-1):
        curr_elem = array[i]
        elems = [curr_elem]
        new_array = array[i+1:]
        new_t = t - curr_elem
        new_elems = is_add_up_to_t_helper(new_array, k-1, new_t)
        
        if new_elems is not None:
            elems.extend(new_elems)
            
        if len(elems) == k:
            return elems
            
    return None