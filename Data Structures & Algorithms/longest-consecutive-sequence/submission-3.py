class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums:
            nums_set = set(nums)
        else:
            return 0

        longest = 1

        for num in nums_set:
            # check if num is start of sequence, if not skip
            if num - 1 in nums_set:
                continue

            # check length of sequence
            curr_longest = 1
            next_value = num + 1
            while next_value in nums_set:
                curr_longest += 1
                longest = max(longest, curr_longest)
                next_value += 1
        
        return longest

        