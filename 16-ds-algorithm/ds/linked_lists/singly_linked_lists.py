class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = self.head
        self.length = 0

    def append(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = self.head
            self.length = 1
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1

    def prepend(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = self.head
            self.length = 1
        else:
            new_node.next = self.head
            self.head = new_node
            self.length += 1

    def insert(self, index, data):
        if index >= self.length:
            if index > self.length:
                print("This position is not available. Inserting at the end of the list")
            self.append(data)
            self.length += 1
        elif index == 0:
            self.prepend(data)
            self.length += 1
        else:
            new_node = Node(data)
            current_node = self.head
            i = 0
            while i != index - 1:
                current_node = current_node.next
                i += 1
            new_node.next = current_node.next
            current_node.next = new_node
            self.length += 1
    
    def remove(self, index):
        if self.head == None:
            print("Linked List is empty. Nothing to delete.")
            return
        elif index == 0:
            self.head = self.head.next
            if self.head == None or self.head.next == None:
                self.tail = self.head
            self.length -= 1
            return
        if index >= self.length:
            index = self.length - 1
        current_node = self.head
        i = 0
        while i != index - 1:
            current_node = current_node.next
            i += 1
        current_node.next = current_node.next.next
        self.length -= 1
        if current_node.next == None:
            self.tail = current_node
        return

    def print_list(self):
        if self.head == None:
            print("Empty")
        else:
            current_node = self.head
            while current_node!= None:
                print(current_node.data, end= ' ')
                current_node = current_node.next


my_linked_list = LinkedList()
my_linked_list.append(10)
my_linked_list.append(100)
my_linked_list.append(1000)
my_linked_list.remove(1)
my_linked_list.print_list()

