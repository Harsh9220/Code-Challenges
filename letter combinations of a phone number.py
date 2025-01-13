class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []

        m={
            "2":["a","b","c"],
            "3":["d","e","f"],
            "4":["g","h","i"],
            "5":["j","k","l"],
            "6":["m","n","o"],
            "7":["p","q","r","s"],
            "8":["t","u","v"],
            "9":["w","x","y","z"]
            }

        def backtrack(index,pattern):
            if index==len(digits):
                res.append("".join(pattern))
                return
            
            for i in m[digits[index]]:
                pattern.append(i)
                backtrack(index+1,pattern)
                pattern.pop()
        res=[]
        backtrack(0,[])        
        return res
        