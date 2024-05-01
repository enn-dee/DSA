# Linear Search in C

Linear Search is a simple searching algorithm that sequentially checks each element in a list until the desired element is found or the end of the list is reached.

## Algorithm

The linear search algorithm iterates through each element in the list and compares it with the target value until a match is found or the end of the list is reached.

1. **Start**: Begin from the first element of the list.
2. **Comparison**: Compare the current element with the target value.
3. **Match**: If the current element matches the target value, return the index of the element.
4. **End of List**: If the end of the list is reached without finding a match, return -1.

## Example

Let's walk through an example to illustrate how linear search works:

**Input List**: [5, 8, 2, 10, 3, 7]
**Target Value**: 10

1. **Step 1 (Start)**: Begin from the first element (5).
2. **Step 2 (Comparison)**: Compare 5 with the target value (10). No match.
3. **Step 3 (Comparison)**: Compare 8 with the target value (10). No match.
4. **Step 4 (Comparison)**: Compare 2 with the target value (10). No match.
5. **Step 5 (Comparison)**: Compare 10 with the target value (10). Match found.
6. **Step 6 (Match)**: Return the index of the matched element (index 3).

**Output**: Index 3 (Element 10 found at index 3)

## Implementation

```c
#include <stdio.h>

// Linear Search function
int linearSearch(int array[], int size, int target) {
    for (int i = 0; i < size; i++) {
        if (array[i] == target) {
            return i; // Element found at index i
        }
    }
    return -1; // Element not found so return -1
}


int main() {
    int array[] = {5, 8, 2, 10, 3, 7};
    int size = sizeof(array) / sizeof(array[0]);
    int target = 10;

    int index = linearSearch(array, size, target);

    if (index != -1) {
        printf("Element %d found at index %d\n", target, index);
    } else {
        printf("Element %d not found in the array\n", target);
    }

    return 0;
}

```
