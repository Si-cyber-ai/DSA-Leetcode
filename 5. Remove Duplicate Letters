class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last = [-1] * 26
        for i in range(len(s)):
            last[ord(s[i]) - 97] = i

        used = [False] * 26   
        stack = []            

        for i in range(len(s)):
            ch = s[i]
            idx = ord(ch) - 97
            if used[idx]:
                continue

            while stack:
                top = stack[-1]
                top_idx = ord(top) - 97

                if ch < top and last[top_idx] > i:
                    stack.pop()
                    used[top_idx] = False
                else:
                    break

            stack.append(ch)
            used[idx] = True

        result = ""
        for c in stack:
            result += c
        return result
