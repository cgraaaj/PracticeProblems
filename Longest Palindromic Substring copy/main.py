class Solution:
    def isValid(self, s):
        dic = {"(": ")", ")": "(", "[": "]", "]": "[", "{": "}", "}": "{"}
        stack = []
        for ch in [c for c in s]:
            if ch in ["(", ")", "{", "}", "[", "]", " "]:
                if len(stack) > 0:
                    if dic[ch] == stack[len(stack)-1]:
                        stack.pop()
                    else:
                        stack.append(ch)
                else:
                    stack.append(ch)
            else:
                return False
        if stack:
            return False
        return True



# Test Program
s = "()(){(())"
# s = "(("
# should return False
print(Solution().isValid(s))

s = ""
# should return True
print(Solution().isValid(s))

s = "([{}])()"
# should return True
print(Solution().isValid(s))
