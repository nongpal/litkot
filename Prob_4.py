class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a = nums1+nums2
        a.sort()

        if len(a)%2:
            idx = len(a) // 2
            return a[idx]
        else:
            idx = len(a) // 2
            r = a[idx-1:idx+1]
            return sum(r)/len(r)
