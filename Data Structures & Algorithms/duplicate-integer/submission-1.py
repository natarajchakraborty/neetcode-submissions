from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counts = Counter(nums)
        if counts and counts.most_common(1)[0][1] > 1:
            return True
        else:
            return False