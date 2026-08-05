class Solution:
    def longestPalindrome(self, s: str) -> str: 
        l = len(s)
        if l == 1:
            return s[0]
        res = s[0]
        best = 1
        for i in range(l):
            for j in range(i+1,l):
                if j-i >= best:
                    sub = s[i:j+1]
                    if sub == sub[::-1]:
                        best = j-i+1
                        res = sub
        return res



   