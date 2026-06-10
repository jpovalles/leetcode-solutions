class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        last_ocurr = dict()
        for j, n in enumerate(nums):
            if n in last_ocurr:
                i = last_ocurr[n]
                if j - i <= k: return True
            last_ocurr[n] = j
        return False
        