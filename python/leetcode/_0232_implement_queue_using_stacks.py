"""
_0232_implement_queue_using_stacks

https://leetcode.com/problems/implement-queue-using-stacks/

Takeaways:

Related problems:

Tags:
#data_struct

"""

class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []
        
    def push(self, x: int) -> None:
        if not self.s1:
            self.front = x
        self.s1.append(x)
        
    def pop(self) -> int:
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())

        return self.s2.pop()

    def peek(self) -> int:
        if self.s2:
            return self.s2[-1]
        return self.front
        
    def empty(self) -> bool:
        return (len(self.s1) + len(self.s2)) == 0
        

def main():

    queue = MyQueue()

    queue.push(1)
    queue.push(2)
    queue.push(3)

    print(queue.empty())

    print(queue.pop())
    print(queue.peek())
    print(queue.pop())

    


if __name__ == '__main__':
    main()