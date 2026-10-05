class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        length = len(nums)
        
        pref = [1 for i in range(length)]
        suff = [1 for i in range(length)]
        res = []

        for i in range(1, length):
            pref[i] = pref[i-1] * nums[i-1]

        for i in range(length - 2, -1, -1):
            suff[i] = suff[i + 1] * nums[i+1]


        for i in range(length):
            res.append(pref[i] * suff[i])
            
        return res
        


