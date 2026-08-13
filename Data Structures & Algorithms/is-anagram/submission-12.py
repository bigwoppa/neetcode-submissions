class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        aas = sorted(s)
        aat = sorted(t)
        if aat == aas:
            return True
        else:
            return False
        