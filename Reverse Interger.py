class Solution:
# @return an integer
    def reverse(self, x):
        import math

        if x<0:
            sign = -1
        else:
            sign = 1
        strx=str(abs(x))
        r = strx[::-1]
        return [sign*int(r), 0][int(r) > math.pow(2,31)]