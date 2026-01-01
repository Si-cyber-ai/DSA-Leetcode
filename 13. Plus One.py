class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        n = len(digits)

        # Start checking from the last digit
        i = n - 1

        while i >= 0:

            # Case 1: digit is less than 9
            if digits[i] < 9:
                digits[i] = digits[i] + 1
                return digits    # no carry needed, stop here

            # Case 2: digit is 9
            # turn it into 0 and carry goes to the left
            digits[i] = 0
            i = i - 1

        # If we exit the loop, all digits were 9
        # Example: [9,9,9] → [1,0,0,0]
        new_digits = [1]
        for d in digits:
            new_digits.append(d)

        return new_digits
