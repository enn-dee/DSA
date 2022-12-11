import java.util.*;
public class BubbleSort {
    public static void main(String[] args) {

        int[] nums = { 5, 1, 4, 2, 8 };
        bubble_sort(nums);
        System.out.println(Arrays.toString(nums)); // [1, 2, 4, 5, 8]

        int[] nums2 = { 1, 2, 3, 4, 5 };
        bubble_sort(nums2);
        System.out.println(Arrays.toString(nums2)); // [1, 2, 3, 4, 5] (already sorted)

        int[] nums3 = { 5, 4, 3, 2, 1 };
        bubble_sort(nums3);
        System.out.println(Arrays.toString(nums3)); // [1, 2, 3, 4, 5] (reverse-sorted)
    }

    public static void bubble_sort(int[] nums) {
        // Set a flag to true to begin the first pass through the list
        boolean swapped = true;

        // Continue looping as long as swapped is true
        while (swapped) {
            // Set swapped to false so that the loop will stop
            // if no swaps are made during this pass
            swapped = false;

            // Loop through the list, comparing adjacent items
            for (int i = 0; i < nums.length - 1; i++) {
                if (nums[i] > nums[i + 1]) {
                    // If the current item is greater than the next item,
                    // swap them and set swapped to true
                    int temp = nums[i];
                    nums[i] = nums[i + 1];
                    nums[i + 1] = temp;
                    swapped = true;
                }
            }
        }
    }

}