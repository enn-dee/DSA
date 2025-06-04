# LIFO (LAST - IN - FIRST -OUT)
# CAN USE LifoQueue (python's queue module - behaves like a stack)
class Node:
    def __init__(self, data):
        self.value = data
        self.next = None
class Stack:
    def __init__(self):
        self.top = None
        self.size =0
        
    def is_empty(self):
        return self.top is None
    
    def push(self,data):
        new_node = Node(data)
        if self.is_empty():
            self.top = new_node
            new_node.next = None
        else:
            new_node.next = self.top
            self.top = new_node
        self.size +=1
    
    def pop(self):
        removed_ele = self.top
        
        if self.is_empty():
            return -1
        else:
            self.top = self.top.next
            
        self.size -=1
        return removed_ele 
    
    def display(self):
        temp_node = self.top
        while temp_node:
            print(temp_node.value, end="->")
            temp_node = temp_node.next
        print("Null")
    
    def peek(self):
        if not self.is_empty():
            
            return self.top.value
        else:
            return -1
        
    def length(self):
        return self.size
            
stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)

stack.display()

print("Top ",stack.peek())

stack.pop()

print("Top ",stack.peek())

print("stack size: ",stack.length())
stack.display()
    