class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = list()
        for i in range(len(nums)):
            n = nums[i]
            if n in diff:
                j = diff.index(n)
                return [j, i]
            diff.append(target-n)