"""
LeetCode Problem 1: Two Sum
Difficulty: Easy

Problem Statement:
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
"""

def two_sum(nums, target):
    """
    Finds two numbers in the array that add up to the target.
    
    :param nums: List of integers.
    :param target: Target integer.
    :return: List containing indices of the two numbers.
    """
    num_map = {}  # Dictionary to store the value and its index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    return []

# Example Test Cases
if __name__ == "__main__":
    test_cases = [
        ([2, 7, 11, 15], 9),
        ([3, 2, 4], 6),
        ([3, 3], 6)
    ]
    
    # We will open a.so to write the output objects as requested
    with open("a.so", "w") as f:
        for nums, target in test_cases:
            result = two_sum(nums, target)
            
            # Print to terminal
            print(f"Input: nums = {nums}, target = {target}")
            print(f"Output: {result}\n")
            
            # Write to a.so
            f.write(f"Input: nums = {nums}, target = {target}\n")
            f.write(f"Output: {result}\n\n")
            
    print("Output has also been saved to 'a.so'")
