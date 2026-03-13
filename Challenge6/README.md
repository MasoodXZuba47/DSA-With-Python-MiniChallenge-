# Challenge 6: 3Sum

## Problem Statement

Given an integer array `nums`, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`. The solution set must not contain duplicate triplets.

## How the Code Works

The problem is solved using a combination of **Sorting** and the **Two-Pointer Technique**. Here is the step-by-step logic:

1. **Sort the array:** We first sort the input array in ascending order. This requires `O(n log n)` time but is essential for easily skipping duplicate numbers to prevent duplicate triplets in our answer. It also enables us to use a two-pointer approach efficiently.
2. **Iterate to anchor the first number:** We use a `for` loop to lock in the first number of our triplet, which we will call `nums[i]`. 
   - Since the array is sorted, if `nums[i]` is greater than 0, we can break out of the loop immediately. Any numbers after `i` will only be larger, so they can never sum to zero.
   - We check `if i > 0 and nums[i] == nums[i-1]` to skip duplicate anchor values, ensuring uniqueness.
3. **Two-pointer search:** For each anchored `nums[i]`, we try to find two other numbers that sum up to `-nums[i]`. We define two pointers:
   - `left` starting right after `i` (`left = i + 1`)
   - `right` starting at the end of the array (`right = len(nums) - 1`)
4. **Evaluating the sum:** We loop as long as `left < right`:
   - Calculate `current_sum = nums[i] + nums[left] + nums[right]`.
   - **If `current_sum < 0`**: The sum is too small. Because the array is sorted, we move the `left` pointer one step to the right to increase the sum.
   - **If `current_sum > 0`**: The sum is too large. We move the `right` pointer one step to the left to decrease the sum.
   - **If `current_sum == 0`**: We've found a valid triplet! We append it to our results list. We then move both pointers inward (`left += 1` and `right -= 1`). To avoid registering duplicate triplets, we run a `while` loop to advance the `left` pointer past any numbers identical to the one we just processed.

### Complexity
- **Time Complexity:** `O(n^2)` — where `n` is the length of the list. We have a primary `for` loop that iterates `n` times, and the two-pointer approach scans the remainder of the array, bringing the total time to `O(n * n) = O(n^2)`.
- **Space Complexity:** `O(1)` or `O(n)` depending on the sorting algorithm memory usage. Python's Timsort uses up to `O(n)` memory. The two-pointer logic itself requires only `O(1)` memory.
