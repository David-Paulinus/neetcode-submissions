class Solution:

    def encode(self, strs: List[str]) -> str:
        result_string = ''

        for string in strs:
            for char in string:
                result_string += str(ord(char))
                result_string += '-1'
            result_string += '-2'

        print(result_string)
        return result_string


    def decode(self, s: str) -> List[str]:
        result = []

        r = 0

        curr_selection = ''
        curr_string = ''
        while r < len(s):
            if s[r] == '-':

                if s[r+1] == '2':
                    result.append(curr_string)
                    curr_string = ''
                else:
                    curr_string += chr(int(curr_selection))

                curr_selection = ''
                r += 2
                continue

            curr_selection += s[r]
            r += 1

        return result


