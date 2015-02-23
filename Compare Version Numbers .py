class Solution:
    # @param version1, a string
    # @param version2, a string
    # @return an integer
    def compareVersion(self, version1, version2):
        num1 = version1.split('.')
        num2 = version2.split('.')
        while (len(num1) or len(num2)):
            if (len(num1) == 0) : num1 = [0]
            if (len(num2) == 0) : num2 = [0]
            else:
                i1 = int(num1[0])
                i2 = int(num2[0])
                if (i1 < i2):
                    return -1
                elif (i1 > i2):
                    return 1
                else:
                    num1 = num1[1:]   ## trim the first part of the arry to continue the iteration 
                    num2 = num2[1:]
                    
        return 0;