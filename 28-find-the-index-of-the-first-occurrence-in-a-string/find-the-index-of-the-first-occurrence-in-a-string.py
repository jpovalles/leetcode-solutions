class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        n = len(haystack)
        m = len(needle)
        lps = self.LPS(needle)
        i = 0; j = 0
        while i < n:
            if needle[j] == haystack[i]:
                i += 1
                j += 1

            if j == m:
                return i-j
                
            elif i < n and needle[j] != haystack[i]:
                if j != 0:
                    j = lps[j - 1]  
                else:
                    i += 1
        return -1

    def LPS(self, s):
        m = len(s)
        lps = [0] * m
        j = 0
        i = 1   

        while i < m:
            if s[i] == s[j]:
                j+=1
                lps[i] = j
                i+=1
            else:
                if j != 0:
                    j = lps[j-1]
                else:
                    lps[i] = 0
                    i+=1
        return lps
        