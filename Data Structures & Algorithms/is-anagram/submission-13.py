class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ss = list(s)
        tt = list(t)
        sorted_s = sorted(ss)
        sorted_t = sorted(tt)
        joined_s = "".join(sorted_s)
        joined_t = "".join(sorted_t)
        print(joined_s, joined_t)
        if joined_s == joined_t:
            return True
        else:
            return False
        