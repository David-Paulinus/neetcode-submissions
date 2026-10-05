class Solution:
    def isValid(self, s: str) -> bool:
        pop_dict = {
            ')': '(', 
            ']': '[', 
            '}': '{'
        }
        stack = []

        for char in s:
            if char not in pop_dict:
                stack.append(char)
            else:
                if not stack:
                    return False
                    
                popped = stack.pop()
                if popped != pop_dict[char]:
                    return False

        if stack:
            return False

        return True
        