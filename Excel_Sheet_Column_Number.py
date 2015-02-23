class Solution:
    # @param s, a string
    # @return an integer
    def titleToNumber(self, s):
        import math
        ans = 0
        t = len(s)
        for i in s:
            ans += (ord(i) - ord('A')+1) * math.pow(26,t-1)   ##26th system is converted to 10th system
            t -= 1
        return int(ans)
            
        