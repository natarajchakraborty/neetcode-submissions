class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = {}
        for n in nums:
            if n in hash:
                hash[n] += 1
            else:
                hash[n] = 1

        sorted_pairs = sorted(hash.items(), key=lambda item: item[1], reverse=True)

        first_k_pairs = sorted_pairs[:k]
        return [key for key, value in first_k_pairs]