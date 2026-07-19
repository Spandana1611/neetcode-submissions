# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rev1(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        
        f = None
        x = head
        i = 0
        while i < k and x:
            temp = x.next
            x.next = f
            f = x          
            x = temp
            i+=1
        if i<k:
            orgn = None
            while f:
                temp = f.next
                f.next = orgn
                orgn = f
                f = temp
            return orgn
        dummy = f
        while dummy.next:
            dummy = dummy.next
        dummy.next = self.rev1(x, k)
        return f

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        return self.rev1(head, k)