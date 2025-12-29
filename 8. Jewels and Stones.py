class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels_set = set(jewels)
        count = 0
        for i in stones:
            if i in jewels_set:
                count += 1
        return count



class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        is_jewel = [0] * 128   # ASCII

        for ch in jewels:
            is_jewel[ord(ch)] = 1

        count = 0
        for ch in stones:
            if is_jewel[ord(ch)] == 1:
                count += 1

        return count
