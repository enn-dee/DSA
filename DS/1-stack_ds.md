**stack** = LIFO data structure. <br/> Last-In First-Out
		            stores objects into a sort of "vertical tower"
	 		        push() to add objects to the top
				    pop() to remove objects from the top
		<img src="https://cdn.discuss.boardinfinity.com/original/2X/9/973c2be769225883ce76291061dcd5ab0d157319.png" height=250px alt="image representation">
**uses of stacks?**
1. undo/redo features in text editors
2. moving back/forward through browser history
3. backtracking algorithms (maze, file directories)
4. calling functions (call stack)

```java	
import java.util.Stack;

public class Main{
	
	public static void main(String[] args) {
		
		
		
		Stack<String> stack = new Stack<String>();
		
		//System.out.println(stack.empty());
		
		stack.push("Minecraft");
		stack.push("Skyrim");
		stack.push("DOOM");
		stack.push("Borderlands");
		stack.push("FFVII");
		
		//String myFavGame = stack.pop();
		//System.out.println(stack.peek());	
		//System.out.println(stack.search("Fallout76"));
		System.out.println(stack);
		
	}
}
```
**Manual implementation Using** -*java* 
```java
// Stack implementation in Java

class Stack {
  private int arr[];
  private int top;
  private int capacity;

  // Creating a stack
  Stack(int size) {
    arr = new int[size];
    capacity = size;
    top = -1;
  }

  // Add elements into stack
  public void push(int x) {
    if (isFull()) {
      System.out.println("OverFlow\nProgram Terminated\n");
      System.exit(1);
    }

    System.out.println("Inserting " + x);
    arr[++top] = x;
  }

  // Remove element from stack
  public int pop() {
    if (isEmpty()) {
      System.out.println("STACK EMPTY");
      System.exit(1);
    }
    return arr[top--];
  }

  // Utility function to return the size of the stack
  public int size() {
    return top + 1;
  }

  // Check if the stack is empty
  public Boolean isEmpty() {
    return top == -1;
  }

  // Check if the stack is full
  public Boolean isFull() {
    return top == capacity - 1;
  }

  public void printStack() {
    for (int i = 0; i <= top; i++) {
      System.out.println(arr[i]);
    }
  }

  public static void main(String[] args) {
    Stack stack = new Stack(5);

    stack.push(1);
    stack.push(2);
    stack.push(3);
    stack.push(4);

    stack.pop();
    System.out.println("\nAfter popping out");

    stack.printStack();

  }
}
```
**Manual implementation Using** - *python* 
```python
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
     return len(self.items) == 0

    def peek(self):
        return self.items[-1]

    def __str__(self):
        return str(self.items)

if __name__ == "__main__":
    stack = Stack()
    print(stack.is_Empty())
  
    stack.push(5)
    print(stack.is_Empty())
  
    stack.push(2)
    stack.push(7)
  
    print(f"Last element is: {stack.peek()}")
    print(f"Removed element: {stack.pop()}")
    print(f"Now last element is: {stack.peek()}")
  
    print(stack)
```

**Revrese String using stack** <br/>
1- Create new file main.py , import stack file (here stackDS)
```python
import stackDS
string = "olleh"
reverse_Word = ""
stck = stackDS.Stack()
for char in string:
    stck.push(char)

while not stck.is_empty():
    reverse_Word += stck.pop()

print(reverse_Word)

  ```
