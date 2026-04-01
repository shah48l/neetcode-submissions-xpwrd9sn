class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            '(' : ')',
            '{' : '}',
            '[' : ']'
        }

        for brack in s:
            if brack in pairs:
                stack.append(brack)
            elif len(stack) == 0 or brack != pairs[stack.pop()]:
                return False

        return len(stack) == 0 