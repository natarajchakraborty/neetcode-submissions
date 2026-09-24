class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {num: index for index, num in reversed(list(enumerate(nums)))}
        
        for index, num in enumerate(nums):
            complement = target - num
            if complement in hash_map and hash_map[complement] != index:
                return sorted([index, hash_map[complement]])
               
        