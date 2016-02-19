

class Node():
    def __init__(self, value):
        self.value = value
        self.next = None


class List():
    def __init__(self):
        self.__firstNode = Node(None)
    def __getLastNode(self):
        pointer = self.__firstNode
        while pointer.next != None:
            pointer = pointer.next
        return pointer
    def __getNode(self, index):
        pointer = self.__firstNode
        position_counter = 0
        while position_counter < index:
            pointer = pointer.next
        return pointer
    def append(self, value):
        if self.__firstNode.value == None:
            self.__firstNode.value = value
        else:
            self.__getLast().next = Node(value)
    def insert(self, position, value):
        pointer = self.__firstNode
        position_counter = 0
        while position_counter < position:
            pointer = pointer.next
        pointer.value = value
    def __getitem__(self, index):
        return self.__getNode(index).value


if __name__ == '__main__':
    l = List()
    l.append(0)
    l.insert(0,5)
    print l[0]


