class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        vals = {
        'I': 1,
        'V':5,
        'X':10,
        'L': 50,
        'C':100,
        'D':500,
        'M':1000
        }
    
        ans = 0
        for i in range(len(s)):
            curr = s[i]
            if i != len(s)-1:
                nxt = s[i+1]
                if vals[curr] >= vals[nxt]: ans += vals[curr]
                else: ans -= vals[curr]
            else: ans += vals[curr]
        return ans
        