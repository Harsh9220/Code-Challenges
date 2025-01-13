class Solution(object):
    def countAsterisks(self, s):
        count=0
        flag = True
        for i in s:
            if flag and i=="*":
                count+=1
            elif i=="|":
                flag=not flag
        return count