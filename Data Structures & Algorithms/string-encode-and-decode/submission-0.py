class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s
        return encoded

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        n = len(s)
        while i < n:
            j = i
            # find the '#' that separates length from string
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            start = j + 1
            result.append(s[start:start + length])
            i = start + length
        return result







