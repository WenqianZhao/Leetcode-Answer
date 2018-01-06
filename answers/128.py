class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        maxValue, hashmap = 1, {}
        for num in nums:
            if not hashmap.has_key(num):
                hashmap[num] = 1
                leftPart = hashmap.get(num-1,0)
                rightPart = hashmap.get(num+1,0)
                hashmap[num-leftPart] = hashmap[num+rightPart] = leftPart+rightPart+1
                maxValue = max(maxValue,leftPart+rightPart+1)
        return maxValue