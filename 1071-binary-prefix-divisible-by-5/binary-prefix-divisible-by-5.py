class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        ans = list()
        n = len(nums)
        suma = 0
        for i in range(n):
            suma *= 2
            if nums[i] == 1: suma += 1
            ans.append(suma % 5 == 0)
        return ans
        