class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        c_sets = set()
        l = 0
        res = 0

        for i in range(len(s)):

            while s[i] in c_sets:
                c_sets.remove(s[l])
                l += 1
            c_sets.add(s[i])
            res = max(res, i-l+1)
            
        return res

        