"""class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sortedList = sorted(nums)
        sequence = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] - nums[i] == 1:
                    sequence += 1
        return sequence"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        store = set(nums)

        for i in nums:
            sequence, curr = 0, i
            while curr in store:
                sequence += 1
                curr += 1
            res = max(res, sequence)
        return res