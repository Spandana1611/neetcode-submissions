# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        i = 0
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            i+=1
        if fast:
            sz = 2*i + 1
        else:
            sz = 2*i
        newhead = ListNode()
        k = newhead
        i = 0
        j = sz-n
        while i < j:
            temp = head.next
            k.next = head
            k = k.next
            head = temp
            i+=1
        head = head.next
        while head:
            temp = head.next
            k.next = head
            k = k.next

            head = temp
        k.next = None
        return newhead.next