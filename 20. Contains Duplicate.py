One Step::

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        h = {}
        for i in range(len(nums)):
            if nums[i] in h:
                return True
            h[nums[i]] = i
        return False


Second Step::
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
