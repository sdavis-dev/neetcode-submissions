class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        match = {")" : "(", "}" : "{", "]" : "["}

        for close in s:
            if close in match:
                if stack and stack[-1] == match[close]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(close)
        
        if not stack:
            return True
        else:
            return False