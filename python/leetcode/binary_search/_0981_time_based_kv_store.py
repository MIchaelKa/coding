"""
_0981_time_based_kv_store

Takeaways:

#data_struct

"""

from typing import List
from collections import defaultdict
import bisect

class TimeMap:
    """
        bisect + list

        + sort() = TLE
        no need for sorting

    """

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        # delayed sorting
        # does specifying key will increase performance if compound values are stored?
        # self.store[key].sort(key=lambda x: x[0])

        # binary search
        index = bisect.bisect_right(self.store[key], timestamp, key=lambda x: x[0])

        if index > 0:
            return self.store[key][index-1][1]
        return ""
    

def main():

    timeMap = TimeMap()

    # 1

    # timeMap.set("foo", "bar1", 4)
    # timeMap.set("foo", "bar1", 1)
    # print(timeMap.get("foo", 1))
    # print(timeMap.get("foo", 3))

    # timeMap.set("foo", "bar2", 4)
    # print(timeMap.get("foo", 4))
    # print(timeMap.get("foo", 5))

    # 2

    # timeMap.set("foo", "A", 4)
    timeMap.set("foo", "B", 1)
    timeMap.set("foo", "A", 4)
    timeMap.set("foo", "C", 7)

    print(timeMap.get("foo", 4))