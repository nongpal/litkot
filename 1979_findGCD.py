class Solution:
    def findGCD(self, nums: List[int]) -> int:
        maximum, minimum = max(nums), min(nums)

        # doing Euclidean Algorithm
        while (minimum != 0):
            reminder = maximum % minimum
            maximum = minimum
            minimum = reminder

        return maximum
