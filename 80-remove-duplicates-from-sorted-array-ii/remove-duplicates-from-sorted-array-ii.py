class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = 1
        cont = 1
        while j < len(nums):
            if nums[j] > nums[i]:
                nums[i+1], nums[j] = nums[j], nums[i+1]
                cont = 1
                i+=1; j+=1
            elif nums[j] == nums[i] and cont < 2:
                nums[i+1], nums[j] = nums[j], nums[i+1]
                i = i+1; j+=1
                cont += 1
            elif nums[j] == nums[i] and cont == 2:
                j+=1
        if len(nums) == 0: return 0 
        return i+1