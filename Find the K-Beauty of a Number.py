class Solution(object):
    def divisorSubstrings(self, num, k):
        """
        :type num: int
        :type k: int
        :rtype: int
        """
        num1=str(num)
        k_beauty=0
        
        for i in range(len(num1)-k+1):
            sub_string=int(num1[i:i+k])
            if sub_string!=0 and num%sub_string==0:
                k_beauty+=1

        return k_beauty