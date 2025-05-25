class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        n = len(nums)
        return len([(i,j) for i in range(n) for j in range(i) if nums[i] == nums[j]])
