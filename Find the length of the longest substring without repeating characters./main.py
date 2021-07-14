class Solution:
    def lengthOfLongestSubstring(self, s):
        temp = []
        longest=""
        now=""
        for i in s:
            if i not in temp:
                now+=i
                temp.append(i)
            else:
                longest = now if len(now)>len(longest) else longest
                temp=[]
                temp.append(i)
                now=i
        return len(longest)
        

print(Solution().lengthOfLongestSubstring('GEEKSFORGEEKS'))