class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
         n = len(temperatures)
        answer = [0] * n       # result array
        stack = []             # stack to store indices

        for i in range(n):

            # While current temperature is higher than
            # the temperature at the index on top of the stack
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_day = stack.pop()
                answer[prev_day] = i - prev_day

            # Push current index onto stack
            stack.append(i)

        return answer
