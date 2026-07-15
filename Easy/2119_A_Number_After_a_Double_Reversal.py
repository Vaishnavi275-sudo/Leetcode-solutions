class Solution(object):
    def isSameAfterReversals(self, num):
        
        rev = int(str(num)[::-1])

        a = int(str(rev)[::-1])

        return (num == a)
        