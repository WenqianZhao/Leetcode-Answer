class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heapq.heapify(nums)
        for _ in xrange(len(nums)-k):
            heapq.heappop(nums)
        return heapq.heappop(nums)