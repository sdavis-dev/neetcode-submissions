class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        useless = set()
        freq = []
        forK = 0

        for i in nums:
            if i in useless:
                if forK < k:
                    freq.append(i)
                    forK += 1
            else:
                useless.add(i)
        return freq