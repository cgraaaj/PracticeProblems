# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    result = None
    def addTwoNumbers(self, l1, l2, c=0):
        v1 = []
        v2 = []
        res = []
        while l1:
            v1.append(l1.val)
            v2.append(l2.val)
            l1 = l1.next
            l2 = l2.next
        v1.reverse()
        v2.reverse()
        v1 = int("".join([str(integer) for integer in v1]))
        v2 = int("".join([str(integer) for integer in v2]))
        res = [int(i) for i in str(v1 + v2)]
        res.reverse()
        for v in res:
            self.insert(v)
        return self.result

    def insert(self,data):
        node = ListNode(data)
        if self.result is None:
            self.result = node
            return
        n = self.result
        while n.next is not None:
            n= n.next
        n.next = node


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = Solution().addTwoNumbers(l1, l2)
while result:
    print(result.val),
    result = result.next
