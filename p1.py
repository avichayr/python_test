

class Node():
    def __init__(self, value):
        self.value = value
        self.next = None
    def __getLast(self):
        pointer = self
        while pointer.next != None:
            pointer = pointer.next
        return pointer
    def append(self, value):
        self.__getLast().next = Node(value)

if __name__ == '__main__':
    n1 = Node(9)
    n1.append(4)
    n1.append(5)

