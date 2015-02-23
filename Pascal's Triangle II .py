class Solution:
    # @return a list of integers
    def getRow(self, rowIndex):
        r = [1]
        for i in xrange(1,rowIndex+1):
          r.append( r[-1]*(rowIndex-i+1)/i )
        return r

'''
recall the related forumla
'''