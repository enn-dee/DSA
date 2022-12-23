import java.util.*;

public class SelectionSort {
  public static void main(String[] args) {
    // Test the selection_sort function
    int[] nums = { 5, 1, 4, 2, 8 };
    selection_sort(nums);
    System.out.println(Arrays.toString(nums)); // [1, 2, 4, 5, 8]

    int[] nums2 = { 1, 2, 3, 4, 5 };
    selection_sort(nums2);
    System.out.println(Arrays.toString(nums2)); // [1, 2, 3, 4, 5] (already sorted)

    int[] nums3 = { 5, 4, 3, 2, 1 };
    selection_sort(nums3);
    System.out.println(Arrays.toString(nums3)); // [1, 2, 3, 4, 5] (reverse-sorted)
  }

  // Implement the selection_sort function
  public static void selection_sort(int[] nums) {
    // Loop through the list, starting at the first element
    for (int i = 0; i < nums.length; i++) {
      // Set the current minimum element to the first element of the unsorted portion
      // of the list
      int minIndex = i;

      // Compare the current minimum element to the remaining elements in the list
      for (int j = i + 1; j < nums.length; j++) {
        // If any element is smaller than the current minimum, set it as the new minimum
        if (nums[j] < nums[minIndex]) {
          minIndex = j;
        }
      }

      // Swap the current minimum element with the first element of the unsorted
      // portion of the list
      int temp = nums[i];
      nums[i] = nums[minIndex];
      nums[minIndex] = temp;
    }
  }
}
