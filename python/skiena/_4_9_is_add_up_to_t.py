from __future__ import annotations
from common.utils import binary_search

def is_add_up_to_t(array: list[int], k: int, t: int) -> list[int]:

    array.sort()
    return is_add_up_to_t_helper(array, k ,t)
    

def is_add_up_to_t_helper(array: list[int], k: int, t: int) -> list[int]:
    
    if k == 1:
        index = binary_search(array, t)
        if index is not None:
            return [array[index]]
        else:
            return None
    
    for x in array:
        elems = [x]
        new_array = array.copy()
        new_array.remove(x)
        new_t = t - x
        new_elems = is_add_up_to_t_helper(new_array, k-1, new_t)
        
        if new_elems is not None:
            elems.extend(new_elems)
            
        if len(elems) == k:
            return elems
            
    return None