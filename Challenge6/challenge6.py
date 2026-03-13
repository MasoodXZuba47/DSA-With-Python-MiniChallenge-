"""
Challenge 6: 3Sum (LeetCode Medium)

Problem Statement:
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
"""

def threeSum(nums: list[int]) -> list[list[int]]:
    """
    Finds all unique triplets in the array which gives the sum of zero.
    
    How it works:
    1. Sort the input array. This is crucial for avoiding duplicates and for the two-pointer approach to work.
    2. Iterate through the array. For each element `nums[i]`, try to find two other elements `nums[left]` 
       and `nums[right]` that sum to `-nums[i]`.
    3. Use two pointers: `left` starting at `i + 1` and `right` starting at the end of the array.
    4. If the sum `nums[i] + nums[left] + nums[right]` is less than zero, move the `left` pointer to the right.
    5. If the sum is greater than zero, move the `right` pointer to the left.
    6. If the sum is exactly zero, we found a triplet. Add it to results, and skip any duplicate 
       `left` values to ensure uniqueness.
    
    Time Complexity: O(n^2) due to the nested loops (one outer, one two-pointer inner).
    Space Complexity: O(1) auxiliary space (excluding the output list and sorting space).
    """
    res = []
    nums.sort()
    
    for i in range(len(nums)):
        # If the current value is greater than zero, we can't sum to zero anymore
        if nums[i] > 0:
            break
            
        # Skip duplicate elements for the first element of our triplet
        if i > 0 and nums[i] == nums[i-1]:
            continue
            
        left, right = i + 1, len(nums) - 1
        
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            
            if current_sum < 0:
                left += 1
            elif current_sum > 0:
                right -= 1
            else:
                res.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                
                # Skip duplicate elements for the second element of our triplet
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                    
    return res
