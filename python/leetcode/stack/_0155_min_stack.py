"""
_0155_min_stack

What if getMin will remove element from the stack?

Takeaways:

#stack, #data_struct

"""

class MinStack:

    def __init__(self):
        self.stack = []      

    def push(self, val: int) -> None:   
        if len(self.stack) == 0 or val < self.stack[-1][1]:
            self.stack.append((val, val))
        else:
            self.stack.append((val, self.stack[-1][1]))
        

    def pop(self) -> None:
        return self.stack.pop()[0]
        

    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.stack[-1][1]      


def main():

    minStack = MinStack()

    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    print(minStack.getMin())
    minStack.pop()
    print(minStack.top())
    print(minStack.getMin())