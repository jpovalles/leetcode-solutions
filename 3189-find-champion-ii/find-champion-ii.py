class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        nums = {i for i in range(n)}
        for u, v in edges:
            nums.discard(v)
        if len(nums) > 1: return -1
        else: return nums.pop()