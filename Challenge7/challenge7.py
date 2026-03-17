"""
Challenge 7: Trapping Rain Water (LeetCode Hard)

Problem Statement:
Given n non-negative integers representing an elevation map where the width
of each bar is 1, compute how much water it can trap after raining.

Example 1:
    Input:  height = [0,1,0,2,1,0,1,3,2,1,2,1]
    Output: 6
    Explanation: The above elevation map (section marked with '#') is represented
                 by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of
                 rain water (section marked with '~') are being trapped.

Example 2:
    Input:  height = [4,2,0,3,2,5]
    Output: 9

Constraints:
    - n == height.length
    - 1 <= n <= 2 * 10^4
    - 0 <= height[i] <= 10^5
"""


def trap(height: list[int]) -> int:
    """
    Calculates the total amount of rain water trapped between the bars.

    Approach — Two Pointer:
    -------------------------
    The key insight is that the water level above any bar at index `i` is
    determined by:
        water[i] = min(max_left[i], max_right[i]) - height[i]

    Instead of pre-computing left/right max arrays (O(n) space), we use two
    pointers (`left` and `right`) that converge from both ends:

    1. Maintain `left_max` and `right_max` tracking the tallest bar seen
       so far from the left and right respectively.
    2. At each step, process the side with the SMALLER max height because
       that side is the bottleneck for how much water can sit on top of it.
    3. If `left_max <= right_max`, the water above `left` = `left_max - height[left]`.
       Move `left` inward.
    4. Otherwise, the water above `right` = `right_max - height[right]`.
       Move `right` inward.
    5. Accumulate the water and repeat until pointers meet.

    Time Complexity:  O(n)  — single pass through the array.
    Space Complexity: O(1)  — only a constant number of variables used.

    Args:
        height (list[int]): Non-negative integers representing bar heights.

    Returns:
        int: Total units of water that can be trapped.
    """
    if not height or len(height) < 3:
        return 0

    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]
    water = 0

    while left < right:
        if left_max <= right_max:
            left += 1
            left_max = max(left_max, height[left])
            water += left_max - height[left]
        else:
            right -= 1
            right_max = max(right_max, height[right])
            water += right_max - height[right]

    return water


# ──────────────────────────────────────────────
#  Helper: visualise the elevation map (ASCII)
# ──────────────────────────────────────────────
def visualize(height: list[int]) -> None:
    """Prints a simple ASCII art of the height map for debugging / display."""
    max_h = max(height)
    print("\n  Elevation Map:")
    for row in range(max_h, 0, -1):
        line = "  "
        for h in height:
            line += "█ " if h >= row else "  "
        print(line)
    print("  " + "─ " * len(height))
    print()


# ──────────────────────────────────────────────
#  Test Cases
# ──────────────────────────────────────────────
if __name__ == "__main__":
    test_cases = [
        {
            "height": [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1],
            "expected": 6,
            "description": "Classic example with multiple pockets"
        },
        {
            "height": [4, 2, 0, 3, 2, 5],
            "expected": 9,
            "description": "Large left and right walls"
        },
        {
            "height": [3, 0, 2, 0, 4],
            "expected": 7,
            "description": "Valley in the middle"
        },
        {
            "height": [1, 0, 1],
            "expected": 1,
            "description": "Minimal trap"
        },
        {
            "height": [0, 0, 0],
            "expected": 0,
            "description": "Flat ground, no water"
        },
        {
            "height": [5],
            "expected": 0,
            "description": "Single bar, no water"
        },
        {
            "height": [1, 2, 3, 4, 5],
            "expected": 0,
            "description": "Strictly increasing — no trapping"
        },
        {
            "height": [5, 4, 3, 2, 1],
            "expected": 0,
            "description": "Strictly decreasing — no trapping"
        },
    ]

    print("=" * 60)
    print("  Challenge 7: Trapping Rain Water")
    print("=" * 60)

    all_passed = True
    for i, tc in enumerate(test_cases, 1):
        result = trap(tc["height"])
        status = "✅ PASS" if result == tc["expected"] else "❌ FAIL"
        if result != tc["expected"]:
            all_passed = False
        print(f"\nTest {i}: {tc['description']}")
        print(f"  Height:   {tc['height']}")
        print(f"  Expected: {tc['expected']}")
        print(f"  Got:      {result}  {status}")

    print("\n" + "=" * 60)
    print(f"  Result: {'All tests passed! 🎉' if all_passed else 'Some tests FAILED ❌'}")
    print("=" * 60)

    # Visual demo for the classic example
    print("\nVisual demo — [0,1,0,2,1,0,1,3,2,1,2,1]:")
    visualize([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
    print(f"  Water trapped: {trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])} units\n")
