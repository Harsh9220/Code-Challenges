class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        diff_candy=set(candyType)
        candy_can_eat=len(candyType)//2

        if candy_can_eat==len(diff_candy):
            return candy_can_eat
        elif candy_can_eat>len(diff_candy):
            return len(diff_candy)
        else:
            candy_num=len(diff_candy)-candy_can_eat
            return len(diff_candy)-candy_num        