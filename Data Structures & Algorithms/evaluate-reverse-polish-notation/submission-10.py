class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        operands = {'+', '-', '*', '/'}

        for token in tokens:
            if token not in operands:
                stack.append(token)
            else:
                snd = int(stack.pop())
                fst = int(stack.pop())

                print(f"{fst} {token} {snd}")

            if token == '+':
                stack.append(fst + snd)
            elif token == '-':
                stack.append(fst - snd)
            elif token == '*':
                stack.append(fst * snd)   
            elif token == '/':
                stack.append(int(fst / snd))

        return int(stack.pop())