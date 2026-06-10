class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ranges = list()
        lims = list()

        for n in nums:
            if not lims: lims.append(n)
            elif n-lims[-1] == 1:
                if len(lims) == 1: lims.append(n)
                else: lims[-1] = n
            else: 
                ranges.append(lims)
                lims = [n]
        if lims: ranges.append(lims)
        return ["->".join(str(i) for i in par) for par in ranges]