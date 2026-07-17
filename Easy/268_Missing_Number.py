class Solution(object):
    def missingNumber(self, nums):
        
        sum = 0
        length = 0

        for num in nums:
            sum += num
        for i in range(1, len(nums)+1):
            length += i

        return length - sum