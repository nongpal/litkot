class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        return sum([1 for i in range(len(nums)) for j in range(i) if (nums[i] + nums[j]) < target])
