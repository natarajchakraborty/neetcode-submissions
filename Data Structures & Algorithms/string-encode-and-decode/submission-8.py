class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s))
            encoded += '#'
            encoded += s
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        lens = ""
        index = 0
        while index < len(s):
            while s[index] != '#':
                lens += s[index]
                index += 1
            leni = int(lens)
            index +=1
            decodedS = s[index : index + leni]
            decoded.append(decodedS)
            index += leni
            lens = ""
        return decoded

