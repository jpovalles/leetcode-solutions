class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(magazine) < len(ransomNote): return False
        else:
            magazineDic = dict()
            for l in magazine:
                if l in magazineDic: magazineDic[l] += 1
                else: magazineDic[l] = 1

            for l in ransomNote:
                if l not in magazineDic: return False
                elif magazineDic[l] == 0: return False
                magazineDic[l] -= 1
            return True