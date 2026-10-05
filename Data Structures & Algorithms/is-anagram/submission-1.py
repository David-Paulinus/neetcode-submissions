class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # return true if the two strings are anagrams of each other, otherwise return false
        # anagrams if they contain the same characters, with each character appearing the same number of times, 
        # regardless of order.

        def dictify(text: str) -> Dict:
            output = {}
            for char in text:
                if char in output:
                    output[char] += 1
                else:
                    output[char] = 1

            return output

        dict_s = dictify(s)
        
        for char in t:
            if char not in dict_s:
                return False

            dict_s[char] -= 1
            if dict_s[char] < 0:
                return False

        for val in dict_s.values():
            if val > 0:
                return False

        return True