class Solution:
    # @return an integer
    def atoi(self, str):
        import math
        if len(str) == 0:
            return 0
        sgn, num, p, x = 0, 0, 0, 0
        imin, imax = -1<<31, (1<<31)-1         #lower and upper limit of integer
        while str[p] == ' ':
            p = p + 1
        if str[p] == '-' or str[p] == '+':
            sgn = 1 if str[p] == '-' else 0
            p = p + +1
        while p < len(str) and str[p]>= '0' and str[p] <= '9':
            num = num *10 + ord(str[p]) - ord('0')
            x = -num if sgn else num
            if x < imin: return imin
            if x > imax: return imax
            p = p + 1
        return x
    
        