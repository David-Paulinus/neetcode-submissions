from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagram_dicts = []
        anagram_groups = []

        def create_anagram_dict(string):
            return Counter(string)

        def check_for_anagram(string, anagram_dict):
            new_anagram_dict = create_anagram_dict(string)
            if new_anagram_dict == anagram_dict:
                return True
            
            return False

        for idx, string in enumerate(strs):
            if idx == 0:
                anagram_dicts.append(create_anagram_dict(string))
                anagram_groups.append([string])
                continue

            found = False
            for i, ana_dict in enumerate(anagram_dicts):
                found = check_for_anagram(string, ana_dict)
                if found:
                    anagram_groups[i].append(string)
                    break

            if not found:
                anagram_dicts.append(create_anagram_dict(string))
                anagram_groups.append([string])

        print(anagram_dicts)
        return anagram_groups
