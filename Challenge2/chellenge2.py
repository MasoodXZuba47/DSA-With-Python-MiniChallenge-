class Solution:
    def threeSum(self, nums):
        """
        Find all unique triplets that sum to zero.
        Time Complexity: O(n^2)
        Space Complexity: O(1) excluding output
        """
        nums.sort()  # Sort to use two pointers and skip duplicates
        result = []
        n = len(nums)
        
        for i in range(n - 2):
            # Skip duplicate values for first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Early termination: if smallest possible sum > 0, break
            if nums[i] + nums[i + 1] + nums[i + 2] > 0:
                break
            
            # Skip if largest possible sum < 0
            if nums[i] + nums[n - 2] + nums[n - 1] < 0:
                continue
            
            # Two pointers approach
            left, right = i + 1, n - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                if current_sum == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # Skip duplicates for second element
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # Skip duplicates for third element
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
                
                elif current_sum < 0:
                    left += 1  # Need larger sum
                else:
                    right -= 1  # Need smaller sum
        
        return result


if __name__ == "__main__":
    sol = Solution()
    
    # Test Case 1
    nums1 = [-1, 0, 1, 2, -1, -4]
    result1 = sol.threeSum(nums1)
    print(f"Input: {nums1}")
    print(f"Output: {result1}")
    print()
    
    # Test Case 2
    nums2 = [0, 1, 1]
    result2 = sol.threeSum(nums2)
    print(f"Input: {nums2}")
    print(f"Output: {result2}")
    print()
    
    # Test Case 3
    nums3 = [0, 0, 0]
    result3 = sol.threeSum(nums3)
    print(f"Input: {nums3}")
    print(f"Output: {result3}")
