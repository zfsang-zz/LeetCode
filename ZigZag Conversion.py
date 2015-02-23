class Solution:
    # @return a string
    def convert(self, s, nRows):
        sf,dire='', 1
        flag=['' for i in range(nRows)]
        if nRows==1:
            return s
        i = 0
        for k in range(len(s)):
            flag[i]+=s[k]
            if(i ==0 and k!=0) or (i==nRows -1):
                dire=-dire
            i+=dire
        for j in range(nRows):
            sf+=flag[j]
        return sf
        
        
'''
思路：
列表flag：记录每一行的字符串
变量i：标记当前字符应该处在的行数
dire：变量i的变化方向，如果触及边界（0和nRows）则dire=-dire
sf：每一行的字符串相加后的最终解
一重循环，时间复杂度O(n)
核心思想：用字符串列表代替二维列表，既解决了空格问题也解决了空间问题。（如果用原字符串和目标字符串之间的数学关系解决，应该也是O（n)而且占用空间小，网上有）
'''