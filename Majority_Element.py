class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
        hashed = {}       # construct a hash table 
        most = len(num) // 2
        for index, value in enumerate(num):
            if value in hashed:
                hashed[value] += 1
            else:
                hashed[value] = 1
            if hashed[value] > most:
                return value