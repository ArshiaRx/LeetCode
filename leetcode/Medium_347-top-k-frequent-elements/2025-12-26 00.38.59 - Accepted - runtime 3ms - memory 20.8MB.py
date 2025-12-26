class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # frequency count
        freq_count = Counter(nums)

        # make a list
        min_heap = []

        # loop through array i
        for index, freq in freq_count.items():

            heapq.heappush(min_heap, (freq, index))

            if len(min_heap) > k:
                heapq.heappop(min_heap)

        return [num for freq, num in min_heap]

        
        