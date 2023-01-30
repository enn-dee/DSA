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
# Creating stack
def create_stack():
    stack = []
    return stack


def is_empty(stack):
    return len(stack) == 0


def push(stack, element):
    stack.append(element)
    print("Inserted ", element)


def pop(stack):
    if (is_empty(stack)):
        print("Stack empty.. ")

    return stack.pop()


stack = create_stack()
push(stack, int(1))
push(stack, int(4))
push(stack, int(5))
print(f"popped item: {pop(stack)}")
print(f"stack after popping an element: {stack} ")

```