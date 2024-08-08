# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def reverse(head):
            prev = None
            curr = head
            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev
        head = reverse(head)
        curr = head
        curr_max = curr.val
        while curr.next:
            if curr.next.val < curr_max:
                curr.next = curr.next.next
                
            else:
                curr_max = curr.next.val
                curr = curr.next
        return reverse(head)
            
        
        