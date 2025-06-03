class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def is_empty(self):
        return self.head == None
    
    def insert_at_beginning(self, data):
        new_node = Node(data)
        
        if self.head:
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = new_node
            self.tail = new_node
    
    def remove_at_beginning(self):
        if self.is_empty():
            return print("Cannot remove. LL  - empty")
        else:
            self.head = self.head.next
    
    def remove_at_end(self):
        if self.is_empty():
            return
        else:
            temp_node = self.head
            while(temp_node.next.next is not None):
                temp_node = temp_node.next
            temp_node.next = None
    
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            temp_node = self.head
            while temp_node.next is not None:
                temp_node = temp_node.next
            temp_node.next = new_node
                
    def display(self):
        temp_node = self.head
        while temp_node:
            
            print(temp_node.data , end="->")
            temp_node = temp_node.next
        print(" NULL")
        
ll = LinkedList()
ll.insert_at_beginning(10)
ll.insert_at_beginning(15)
ll.insert_at_beginning(20)
ll.insert_at_beginning(30)
ll.insert_at_beginning(40)
ll.insert_at_beginning(50)

ll.insert_at_end(60)

ll.remove_at_beginning()

ll.remove_at_end()

ll.display()