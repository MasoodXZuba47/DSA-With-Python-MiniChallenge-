"""
Challenge 5: Trapping Rain Water (LeetCode Hard)

Problem Statement:
Given n non-negative integers representing an elevation map where the width of each bar is 1, 
compute how much water it can trap after raining.

Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. 
In this case, 6 units of rain water are being trapped.

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9

Constraints:
n == height.length
1 <= n <= 2 * 10^4
0 <= height[i] <= 10^5
"""

def trap(height: list[int]) -> int:
    """
    Computes the amount of water trapped using the Two-Pointer approach.
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if not height:
        return 0
        
    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]
    water_trapped = 0
    
    while left < right:
        if left_max < right_max:
            left += 1
            left_max = max(left_max, height[left])
            water_trapped += left_max - height[left]
        else:
            right -= 1
            right_max = max(right_max, height[right])
            water_trapped += right_max - height[right]
            
    return water_trapped

if __name__ == "__main__":
    # Test cases
    test_cases = [
        ([0,1,0,2,1,0,1,3,2,1,2,1], 6),
        ([4,2,0,3,2,5], 9),
        ([1,2,3,4,5], 0),  # strictly increasing (cannot trap water)
        ([5,4,3,2,1], 0),  # strictly decreasing (cannot trap water)
        ([3,0,0,2,0,4], 10), # deep bucket
        ([], 0)            # empty array
    ]

    print("--- Trapping Rain Water Solution ---")
    for i, (height, expected) in enumerate(test_cases, 1):
        result = trap(height)
        status = "✅ PASSED" if result == expected else f"❌ FAILED (Expected: {expected}, Got: {result})"
        print(f"Test case {i}: {status}\n  Input: {height}\n  Output: {result}\n")
