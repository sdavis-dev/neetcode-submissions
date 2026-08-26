class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for i in s:
            if i == "(":
                stack.append("(")
            if i == ")":
                if "(" in stack:
                    stack.remove("(")
            if i == "{":
                stack.append("{")
            if i == "}":
                if "{" in stack:
                    stack.remove("{")
            if i == "[":
                stack.append("[")
            if i == "]":
                if "[" in stack:
                    stack.remove("[")
        if not stack:
            return True
        else:
            return False



        