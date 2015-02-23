class Solution:
    # @return a boolean
    def isValid(self, s):
        dct = {'(':')', '[':']','{':'}'}
        stk=[]
        for c in s:
            if dct.get(c, None):
                stk.append(c)           #append first part of parentheses ([{  (keys)
            elif len(stk) == 0 or dct[stk[-1]] != c:
                return False
            else: 
                stk.pop()        #remove a parenthese from stk list if matched
        return True if len(stk) == 0 else False