class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        ans = A[0]
        for i in xrange(1, len(A)):
            ans = ans ^ A[i]
        return ans
        
        
'''
解题思路：这题考的是位操作。只需要使用异或(xor)操作就可以解决问题。异或操作的定义为：x ^ 0 = x; x ^ x = 0。用在这道题里面就是：y ^ x ^ x = y; x ^ x = 0; 举个例子：序列为：1122334556677。4是那个唯一的数，之前的数异或操作都清零了，之后的数：4 ^ 5 ^ 5 ^ 6 ^ 6 ^ 7 ^ 7 = 4 ^ ( 5 ^ 5 ^ 6 ^ 6 ^ 7 ^ 7 ) = 4 ^ 0 = 4。问题解决。
'''