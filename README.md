# 🧠 Two Sum - LeetCode Problem

## 📌 Problem Statement

Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to `target`.

You may assume:
- Each input has exactly one solution.
- You may not use the same element twice.
- You can return the answer in any order.

---

## 🔎 Example

Input:
nums = [2,7,11,15]
target = 9

Output:
[0,1]

Explanation:
nums[0] + nums[1] = 2 + 7 = 9

---

## 🚀 Approach

We use a HashMap (dictionary) to store numbers and their indices while iterating.

For each number:
1. Compute complement = target - num
2. Check if complement exists in dictionary
3. If yes → return indices
4. Otherwise → store current number in dictionary

This avoids nested loops.

---

## 💻 Python Solution

```python
class Solution:
    def twoSum(self, nums, target):
        hashmap = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            
            if complement in hashmap:
                return [hashmap[complement], i]
            
            hashmap[num] = i
