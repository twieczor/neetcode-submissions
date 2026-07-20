class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        map_open = {")" : "(", "]" : "[", "}" : "{"}

        for c in s:
            if c in map_open:
                if stack and stack[-1] == map_open[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False

