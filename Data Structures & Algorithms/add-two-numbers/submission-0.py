# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a = 0
        b = 0
        i = 0
        x = l1
        while x:
            a += x.val*(10**i)
            i+=1
            x = x.next
        x = l2
        i = 0
        while x:
             b+= x.val*(10**i)
             i+=1
             x = x.next
        a = int(a)
        b = int(b)
        c = str(a+b)[::-1]
        ans = ListNode()
        x = ans
        for i in c:
            x.next = ListNode(int(i))
            x = x.next
        return ans.next