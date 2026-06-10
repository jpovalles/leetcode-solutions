class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        ans = False
        if len(s) == len(t):
            maping = dict()
            for i in range(len(s)):
                char_s = s[i]
                char_t = t[i]
                if char_s in maping:
                    if maping[char_s] != char_t: return False
                else:
                    if char_t in maping.values(): return False
                    maping[char_s] = char_t
            ans = True
        return ans
        