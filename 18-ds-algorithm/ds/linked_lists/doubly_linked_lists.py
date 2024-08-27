class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

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
            new_node.previous = self.tail
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
            self.head.previous = new_node
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
            new_node.previous = current_node
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

    def reverse(self):
        if not self.head or not self.head.next:
            return self

        first = self.head
        second = first.next
        self.tail = self.head
        while second:
            temp = second.next
            second.next = first
            first = second
            second = temp
        self.head.next = None
        self.head = first
        return self
            

my_linked_list = LinkedList()
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)
my_linked_list.append(6)
my_linked_list.print_list()
print('')
my_linked_list.reverse()
my_linked_list.print_list()

