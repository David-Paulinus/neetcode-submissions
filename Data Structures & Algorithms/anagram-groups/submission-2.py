class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        '''
        
        '''

        def freqTuple(s):
            a = [0] * 26
            for char in s:
                idx = ord(char) - ord('a')
                a[idx] += 1
            
            return tuple(a)

        groups = {} # freqTuple -> [String]

        for s in strs:
            tup = freqTuple(s)
            
            if tup not in groups:
                groups[tup] = [s]
            else:
                groups[tup].append(s)

        output = []
        for v in groups.values():
            output.append(v)

        return output


        