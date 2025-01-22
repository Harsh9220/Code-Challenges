class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse_code={
            "a":".-",
            "b":"-...",
            "c":"-.-.",
            "d":"-..",
            "e":".",
            "f":"..-.",
            "g":"--.",
            "h":"....",
            "i":"..",
            "j":".---",
            "k":"-.-",
            "l":".-..",
            "m":"--",
            "n":"-.",
            "o":"---",
            "p":".--.",
            "q":"--.-",
            "r":".-.",
            "s":"...",
            "t":"-",
            "u":"..-",
            "v":"...-",
            "w":".--",
            "x":"-..-",
            "y":"-.--",
            "z":"--.."}

        transformation_list=[]

        for i in words:
            output=''
            for j in i:
                output+=morse_code[j]
            transformation_list.append(output)

        diff_transformation=list(set(transformation_list))
        
        return len(diff_transformation)