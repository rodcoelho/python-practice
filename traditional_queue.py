# not using Python lists
class Node(object):
    def __init__(self, other=None):
        self.other = other
        self.next = None
        self.previous = None

    def __str__(self):
        return str(self.other)

class List(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        newNode = Node(value)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            newNode.previous = self.tail
            self.tail = newNode

    def printlist(self):
        temp = self.head
        while temp is not None:
            print(temp)
            temp = temp.next

class Queue(List):
    def enqueue(self,value):
        self.append(value)

    def dequeue(self):
        self.temp = self.head
        self.head = self.head.next
        return self.temp

if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(10)
    q.enqueue(100)
    q.enqueue(1000)
    q.enqueue(10000)
    q.enqueue(100000000000)
    q.printlist()
    print()
    x = q.dequeue()
    print(x)