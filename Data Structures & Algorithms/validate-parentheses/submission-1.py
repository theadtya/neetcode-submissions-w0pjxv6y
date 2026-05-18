class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for curr_char in s:
            if curr_char in "({[":
                stack.append(curr_char)
            else:
                if not stack:
                    return False
                prev_char= stack.pop()
                if curr_char == ")" and prev_char !="(":
                    return False
                elif curr_char == ")" and prev_char !="(":
                    return False
                elif curr_char == "]" and prev_char !="[":
                    return False
        return len(stack)==0



