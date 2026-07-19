# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ans = ListNode()
        head = ans
        while len(lists)>0 and lists[0] is None:
            lists = lists[1:]
        if len(lists) == 0:
            return None
        while len(lists)>0 and lists[0] is not None:
            x = lists[0].val
            x_idx = 0
            i = 1
            while i<len(lists):
                if lists[i]:
                    if x > lists[i].val:
                        x = lists[i].val
                        x_idx = i
                i+=1
            head.next = ListNode(x)
            lists[x_idx] = lists[x_idx].next
            head = head.next
            while len(lists)>0 and lists[0] is None:
                lists = lists[1:]
        return ans.next