class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nums[i] + nums[j] == target and i != j
        # every input has exactly one pair of indices i and j
        # Return the answer with the smaller index first. return [i, j]

        seen = {} # store num -> idx

        for idx, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], idx]
            else:
                seen[num] = idx
    
