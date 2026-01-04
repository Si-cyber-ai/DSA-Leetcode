####################### WITHOUT SET AND MATH
class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        total_sum = 0

        for num in nums:
            divisors = []   # list to store divisors

            i = 1
            while i * i <= num:
                if num % i == 0:
                    divisors.append(i)

                    if i != num // i:
                        divisors.append(num // i)

                # early stop if more than 4 divisors
                if len(divisors) > 4:
                    break

                i += 1

            if len(divisors) == 4:
                s = 0
                for d in divisors:
                    s += d
                total_sum += s

        return total_sum

############################# WITH SET AND IMPORT MATH
import math
class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        total_sum = 0

        for num in nums:
            divisors = set()

            # check divisors up to sqrt(num)
            for i in range(1, int(math.sqrt(num)) + 1):
                if num % i == 0:
                    divisors.add(i)
                    divisors.add(num // i)

                # early stop if more than 4 divisors
                if len(divisors) > 4:
                    break

            if len(divisors) == 4:
                total_sum += sum(divisors)

        return total_sum
