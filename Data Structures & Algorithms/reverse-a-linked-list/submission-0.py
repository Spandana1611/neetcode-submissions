# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head

        l = []
        while head.next :
            l.append(head.val)
            head = head.next
        l.append(head.val)
        if len(l) == 0:
            return ListNode()
        j = len(l)-1
        ans = ListNode(l[j])
        p = ans
        j-=1
        while j>=0:
            a = ListNode(l[j])
            p.next = a
            p = a
            j-=1
        return ans
