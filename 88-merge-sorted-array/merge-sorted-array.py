class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m-1
        j = n-1
        u = len(nums1)-1
        while j >= 0:
            a = float("-inf")
            if i >= 0: a = nums1[i]
            b = nums2[j]
            if b >= a or i < 0:
                nums1[u] = b
                j -=1
            else:
                nums1[u] = a
                nums1[i] = 0
                i-=1
            u -= 1