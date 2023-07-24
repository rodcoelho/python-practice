class Node(object):
    def __init__(self,d, n):
        self.data = d
        self.next = n
    def __str__(self):
        return str(self.data)

class LinkedList(object):
        def __init__(self):
            self.first = None
        def insert(self, data):
            self.first = Node(data,self.first)
        def size(self):
            count = 0
            pointer = self.first
            while pointer != None:
                count += 1
                pointer = pointer.next
            return count
        def search(self, target):
            pointer = self.first
            while pointer != None:
                if pointer.data == target:
                    return True
                pointer = pointer.next
            return False

if __name__ == "__main__":
    ll = LinkedList()

    # insert test
    for i in range(100):
        ll.insert(i)
    print(ll.size())
    ll.insert(42)

    # search test
    x = ll.search(42)
    print(x)

    # size test
    y = ll.size()
    print(y)
