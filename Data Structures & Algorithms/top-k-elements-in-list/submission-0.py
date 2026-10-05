from heapq import heappop, heappush, heapify
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    
        frequencies = Counter(nums)
        frequencies = [(value * -1, key) for key, value in frequencies.items()]
        heapify(frequencies)

        result = []
        for i in range(k):
            result.append(heappop(frequencies)[1])

        return result

        