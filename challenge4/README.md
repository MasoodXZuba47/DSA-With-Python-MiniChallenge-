# Challenge 4: Container With Most Water 🌊

This repository contains the Python solution for the popular LeetCode problem **[11. Container With Most Water]**.

## 📝 Problem Description

You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `i`th line are `(i, 0)` and `(i, height[i])`.

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

**Note:** You may not slant the container.

### Example 1:
**Input:** `height = [1,8,6,2,5,4,8,3,7]`
**Output:** `49`
**Explanation:** The vertical lines are positioned at indices `[1,8,6,2...7]` depending on values. The max area is formed between the lines at index 1 (height 8) and index 8 (height 7). `min(8, 7) * (8 - 1) = 49`.

### Example 2:
**Input:** `height = [1,1]`
**Output:** `1`

## 💡 Solution Explanation

The problem is solved using the **Two-Pointer** approach to ensure an optimal **O(n)** time complexity.

1. **Initialize two pointers:** `left` at the beginning (index 0) and `right` at the end (index `n-1`) of the array.
2. **Calculate area:** At each step, calculate the area formed by the lines at the two pointers: `Area = min(height[left], height[right]) * (right - left)`.
3. **Update Maximum Area:** Keep track of the maximum area seen so far.
4. **Move the pointer:** The height of the container is limited by the shorter line. Therefore, to possibly find a larger area, we move the pointer that points to the shorter line inward.
5. Repeat until the two pointers meet.

## 🚀 Complexity Analysis
- **Time Complexity:** `O(n)` — We traverse the array exactly once.
- **Space Complexity:** `O(1)` — Only constant extra space is used for the pointers and the `max_area` variable.

## 🛠️ How to Run

1. Ensure you have Python installed on your system.
2. Clone this repository or download the `chellenge4.py` file.
3. Open a terminal or command prompt.
4. Run the script using the following command:
   ```bash
   python chellenge4.py
   ```
5. The script includes built-in test cases that will automatically run and verify the correctness of the solution.
