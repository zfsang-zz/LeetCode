class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        import math
        imin, imax = -1<<31, (1<<31)-1
        sgn = -1 if x<0 else 1
        x = sgn*x
        res = (str(x)[::-1]) == str(x)
        if x < imin or x > imax:      ##outflow check
            return False
        return res if sgn == 1 else False
        