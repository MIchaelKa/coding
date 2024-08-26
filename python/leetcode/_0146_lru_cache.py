"""
_0146_lru_cache

Takeaways:
- implement helper methods early

TODO:

Related problems:

Tags:
#design

"""

from typing import List

class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class LRUCache:
    """
        Linked list.
    """
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = None
        self.tail = None

    def delete(self, node: Node):
        if node.next and node.prev:
            node.next.prev = node.prev
            node.prev.next = node.next
        elif node.next:
            node.next.prev = None
            self.head = node.next
        elif node.prev:
            node.prev.next = None
            self.tail = node.prev
        else:
            self.head = None
            self.tail = None

    def add(self, node: Node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            node.next = None # need for already added nodes
            self.tail = node
        
    def get(self, key: int) -> int:
        # node = self.head
        # while node:
        #     print(node.key, node.value)
        #     node = node.next
        # print()

        if key in self.cache:
            node = self.cache[key]
            self.delete(node)
            self.add(node)
            return self.tail.value
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self.delete(node)  
            self.add(node)
            node.value = value
        else:         
            node = Node(key, value)
            self.add(node)
            self.cache[key] = node

            if len(self.cache) > self.capacity:
                self.cache.pop(self.head.key)
                self.delete(self.head)

        # for k, v in self.cache.items():
        #     print(k, v.key, v.value)



def run_tests(solution):
    print("test passed!")

def test_1():
    cache = LRUCache(2)

    cache.put(1, 1) # cache is {1=1}
    cache.put(2, 2) # cache is {1=1, 2=2}
    print(cache.get(1)) # return 1

    cache.put(3, 3) # cache is {1=1, 3=3}
    print(cache.get(2)) # return -1

    cache.put(4, 4) # cache is {4=4, 3=3}
    print(cache.get(1)) # return -1
    print(cache.get(3)) # return 3
    print(cache.get(4)) # return 4

    cache.put(4, 5) # cache is {4=5, 3=3}
    print(cache.get(4)) # return 5

def test_2():
    cache = LRUCache(2)

    cache.put(2, 1) # cache is {2=1}
    cache.put(3, 2) # cache is {3=2, 2=1}

    print(cache.get(3)) # return 2
    print(cache.get(2)) # return 1

    cache.put(4, 3) # cache is {4=3, 2=1}
    print(cache.get(2)) # return 1
    print(cache.get(3)) # return -1
    print(cache.get(4)) # return 3

def test(methods, values):
    for m, v in zip(methods, values):
        if m == "LRUCache":
            cache = LRUCache(v[0])
        elif m == "put":
            cache.put(*v)
        elif m == "get":
            print(cache.get(v[0]))

    

def test_3():
    cache = LRUCache(2)
    cache.put(2, 1) # cache is {2=1}
    print(cache.get(2)) # return 1

def main():
    # test_1()
    # test_2()
    # test_3()

    methods = ["LRUCache","put","put","put","put","get","get","get","get","put","get","get","get","get","get"]
    values = [[3],[1,1],[2,2],[3,3],[4,4],[4],[3],[2],[1],[5,5],[1],[2],[3],[4],[5]]
    test(methods, values)
    


if __name__ == '__main__':
    main()