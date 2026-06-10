class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        j = len(nums)-1
        while i <= j:
            if nums[i] == val:
                nums[i] = nums[j]
                nums[j] = val
                nums.pop()
            else:
                i+=1
            j = len(nums)-1
        return len(nums) 