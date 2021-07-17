class Solution: 
    def getRange(self, arr, target):
        res = []
        try:
            arr.index(target)
            res.append(arr.index(target))
        except:
            res.append(-1)
        arr.reverse()
        try:
            arr.index(target)
            res.append(len(arr)-1-arr.index(target))
        except:
            res.append(-1)
        return res
  
# Test program 
arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8] 
x = 8
print(Solution().getRange(arr, x))
# [1, 4]