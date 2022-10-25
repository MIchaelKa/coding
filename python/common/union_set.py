

class UnionSet:
    def __init__(self, n: int):
        self.parents = list(range(n))
        self.size = [1] * n

    def find(self, x: int) -> int:
        if self.parents[x] == x:
            return x
        
        return self.find(self.parents[x])
    
    def union(self, x: int, y: int):

        comp_1 = self.find(x)
        comp_2 = self.find(y)

        if comp_1 == comp_2:
            return
        
        if self.size[comp_1] >= self.size[comp_2]:
            self.parents[comp_2] = comp_1
            self.size[comp_1] += self.size[comp_2]
        else:
            self.parents[comp_1] = comp_2
            self.size[comp_2] += self.size[comp_1]

    def same_component(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)


if __name__ == '__main__':

    union_set = UnionSet(10)

    result = union_set.find(4)
    assert(result == 4)

    union_set.union(3,4)
    union_set.union(7,8)

    result = union_set.find(4)
    assert(result == 3)

    result = union_set.find(8)
    assert(result == 7)

    union_set.union(7,3)
    result = union_set.find(4)
    assert(result == 7)

    union_set.union(7,3)
    assert(union_set.same_component(3,8))
