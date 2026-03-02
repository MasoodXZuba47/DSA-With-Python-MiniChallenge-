# 🧠 Challenge 1 – Two Sum

## Problem Statement

Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to `target`.

Constraints:
- Each input has exactly one solution.
- You may not use the same element twice.
- The answer can be returned in any order.

---

## Example

Input:
nums = [2, 7, 11, 15]
target = 9

Output:
[0, 1]

Explanation:
nums[0] + nums[1] = 2 + 7 = 9

---

## Approach

A brute-force approach would use two nested loops, resulting in O(n²) time complexity.

Instead, this solution uses a HashMap (Python dictionary) to reduce time complexity to O(n).

### Algorithm Steps:

1. Create an empty dictionary to store numbers and their indices.
2. Iterate through the list using enumerate().
3. For each number:
   - Compute complement = target - current number.
   - Check if complement exists in the dictionary.
   - If it exists → return stored index and current index.
   - If not → store the current number with its index.
4. Continue until solution is found.

This ensures only one pass through the array.

---

## Time Complexity

O(n)  
Each element is visited once.

---

## Space Complexity

O(n)  
Dictionary stores at most n elements.

---

## Python Implementation

class Solution:
    def twoSum(self, nums, target):
        hashmap = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            
            if complement in hashmap:
                return [hashmap[complement], i]
            
            hashmap[num] = i


if __name__ == "__main__":
    sol = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    result = sol.twoSum(nums, target)
    print("Output:", result)

---

## Key Concepts Used

- HashMap (Dictionary)
- One-pass traversal
- Time optimization
- Efficient lookup (O(1) average case)
