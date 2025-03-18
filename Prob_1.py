class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}
        n = len(nums)

        for i in range(n):
            comp = target - nums[i]
            if comp in table:
                return [table[comp], i]
            table[nums[i]] = i
