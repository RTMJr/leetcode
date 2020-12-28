class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        pairs = 0
        count = 0
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i] == nums[i - 1]:
                count += 1
                pairs += count
            else:
                count = 0
        return pairs
