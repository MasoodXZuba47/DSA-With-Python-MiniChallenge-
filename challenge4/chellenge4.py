"""
LeetCode Problem 11: Container With Most Water
Difficulty: Medium

Description:
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.
"""

def maxArea(height: list[int]) -> int:
    """
    Calculates the maximum area of a container formed by two lines.
    
    Time Complexity: O(n) where n is the length of the height array.
    Space Complexity: O(1) as we only use two pointers.
    """
    left = 0
    right = len(height) - 1
    max_area = 0
    
    while left < right:
        # Calculate the current area
        current_area = min(height[left], height[right]) * (right - left)
        # Update max_area if current_area is larger
        max_area = max(max_area, current_area)
        
        # Move the pointer pointing to the shorter line to potentially find a taller line
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
            
    return max_area

if __name__ == "__main__":
    # Test cases
    test_cases = [
        ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
        ([1, 1], 1),
        ([4, 3, 2, 1, 4], 16),
        ([1, 2, 1], 2)
    ]
    
    print("--- Testing Container With Most Water ---")
    for i, (height, expected) in enumerate(test_cases, 1):
        result = maxArea(height)
        status = "PASSED" if result == expected else "FAILED"
        print(f"Test Case {i}: {status}")
        print(f"  Input: height = {height}")
        print(f"  Expected: {expected}, Got: {result}\n")
