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
        dict_t = dictify(t)

        if dict_s == dict_t:
            return True
        else:
            return False