from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            count_s = Counter(s)
            count_t = Counter(t)
            for key in count_s:
                if count_s[key] != count_t[key]:
                    return False
        
        return True
