class Solution:
    def twoSum(self, nums, target):
        hashmap = {}  # number -> index
        
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