class Solution(object):
    def sortedSquares(self, nums):
        
        a=[]

        for num in nums:
            x = num**2
            a.append(x)
            num += 1
        a.sort()

        return a
        