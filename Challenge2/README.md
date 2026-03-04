# 3Sum - LeetCode Problem 15

## Problem Statement

Given an integer array `nums`, return all the unique triplets `[nums[i], nums[j], nums[k]]` such that:
- `i != j`, `i != k`, and `j != k`
- `nums[i] + nums[j] + nums[k] == 0`

Notice that the solution set must not contain duplicate triplets.

## Examples

**Example 1:**
```
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
```

**Example 2:**
```
Input: nums = [0,1,1]
Output: []
```

**Example 3:**
```
Input: nums = [0,0,0]
Output: [[0,0,0]]
```

## Solution Approach

### Two Pointers Technique

1. **Sort the array** - This enables the two-pointer approach and makes duplicate detection easier
2. **Fix one element** - Iterate through the array, fixing `nums[i]` as the first element
3. **Two pointers for remaining sum** - Use `left` and `right` pointers to find pairs that sum to `-nums[i]`
4. **Skip duplicates** - At each level, skip duplicate values to ensure unique triplets

### Complexity Analysis

- **Time Complexity:** O(n²) - Sorting takes O(n log n), and the nested loop with two pointers is O(n²)
- **Space Complexity:** O(1) - Excluding the output array, we use constant extra space

## Key Insights

- Sorting transforms the problem from needing a hash set to using two pointers
- Early termination conditions optimize performance:
  - If `nums[i] + nums[i+1] + nums[i+2] > 0`, break (smallest possible sum too large)
  - If `nums[i] + nums[n-2] + nums[n-1] < 0`, continue (largest possible sum too small)

## Code

See [chellenge2.py](chellenge2.py) for the implementation.

## Running the Code

```bash
python chellenge2.py
```
