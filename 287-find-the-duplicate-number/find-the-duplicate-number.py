class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        check = set()
        for num in nums:
            if num in check: return num
            else: check.add(num)