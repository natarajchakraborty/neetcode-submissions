class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}
        for s in strs:
            arr = [0] * 26
            for c in s:
                arr[ord(c) - ord('a')] += 1
            key = tuple(arr)
            if key in hashMap:
                hashMap[key].append(s)
            else:
                hashMap[key] = [s]
        return list(hashMap.values())