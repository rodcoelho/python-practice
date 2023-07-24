# not using Python lists
class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    def __str__(self):
        return str(self.data)

class StackedLinkedList(object):
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, value):
        item = Node(value)
        item.next = self.head
        self.head = item

    def pop(self):
        if self.head == None:
            return None
        first = self.head
        value = self.head
        self.head = first.next
        return value

    def isEmpty(self):
        return not self.head

    def printList(self):
        n = self.head
        while n:
            print(str(n))
            n = n.next

    def peek(self):
        n = self.head
        count = self.size
        while count > 0:
            n = n.next
            count -=1
        print(n)

if __name__ == "__main__":
    sll = StackedLinkedList()
    sll.push('a')
    sll.push('b')
    sll.push('cat')
    sll.push('bobby')
    sll.push('ricky')
    sll.printList()
    sll.pop()
    sll.pop()
    sll.pop()
    sll.pop()
    sll.printList()