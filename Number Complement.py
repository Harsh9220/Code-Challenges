class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        def deci_bin(num):
            return format(num,'b')

        bin_num=deci_bin(num)
        complement_num=''
        for i in bin_num:
            if i=="0":
                complement_num+="1"
            else:
                complement_num+="0"    
        return int(complement_num,2)