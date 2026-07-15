# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        if list1.val <= list2.val:
            newhead = ListNode(list1.val)
            list1 = list1.next
            if list1 is None:
                newhead.next = list2
                return newhead
        else:
            newhead = ListNode(list2.val)
            list2 = list2.next
            if list2 is None:
                newhead.next = list1
                return newhead
        curr = newhead
        while list1.next and list2.next:
            if list1.val <= list2.val:
                curr.next = ListNode(list1.val)
                curr = curr.next
                list1 = list1.next
            else:
                curr.next = ListNode(list2.val)
                curr = curr.next
                list2 = list2.next
        if list1.next is not None:
            while list1.next and list2.val>list1.val:
                curr.next = ListNode(list1.val)
                curr = curr.next
                list1 = list1.next
            if list2.val > list1.val:
                curr.next = list1
                curr.next.next = list2
                return newhead
            curr.next = list2
            curr.next.next = list1
            return newhead
        while list2.next and list1.val>list2.val:            
            curr.next = ListNode(list2.val)
            curr = curr.next
            list2 = list2.next
        if list1.val > list2.val:
            curr.next = list2
            curr.next.next = list1
            return newhead
        curr.next = list1
        curr.next.next = list2
        return newhead