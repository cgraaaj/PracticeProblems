class Solution: 
    def longestPalindrome(self, s):
        res=""
        for i,ch in enumerate(s):
            if ch in s[i+1:len(s)]:
                rev = s[i:len(s)][::-1]
                for j,c in enumerate(rev):
                    if c in rev[j+1:len(rev)]:
                        recent = rev[j:len(rev)]
                        res = recent if len(recent)>len(res) else res
                        break
        return res

        
# Test program
s = "million"
# print(s[2:len(s)])
print(str(Solution().longestPalindrome(s)))
# racecar