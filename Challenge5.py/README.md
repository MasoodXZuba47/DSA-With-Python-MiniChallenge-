# Challenge 5: Trapping Rain Water 🌧️

## Difficulty: Hard
**Platform:** LeetCode

## Problem Statement 📝
Given `n` non-negative integers representing an elevation map where the width of each bar is `1`, compute how much water it can trap after raining.

**Example 1:**
```text
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The elevation map is represented by the array. In this case, 6 units of rain water are being trapped.
```

**Example 2:**
```text
Input: height = [4,2,0,3,2,5]
Output: 9
```

## Approach & Algorithm 🧠
This solution employs the highly efficient **Two Pointers** technique to solve the problem in a single pass.

* Instead of finding the maximum height to the left and right of each element using extra arrays (which takes `O(N)` space), we can use two pointers (`left` and `right`).
* We maintain `left_max` and `right_max` variables.
* Since the trapped water at any bar depends on the *minimum* of the maximum heights on its left and right, we can safely process the side with the smaller maximum height.
* If `left_max < right_max`, the water trapped depends strictly on `left_max`. We increment `left`, update `left_max`, and add the trapped water. Otherwise, we do the equivalent for the right side.

## Complexity Analysis ⏱️
- **Time Complexity:** `O(N)` where `N` is the length of the `height` array. We traverse the array exactly once using the two pointers.
- **Space Complexity:** `O(1)`. We only use a few variables (`left`, `right`, `left_max`, `right_max`, `water_trapped`) requiring constant extra space.

## Running the Code 💻
Make sure you have Python installed. You can run the code from your terminal using the following command:

```bash
python challenge5.py
```

The script includes multiple test cases to automatically verify the correctness of the algorithm.
