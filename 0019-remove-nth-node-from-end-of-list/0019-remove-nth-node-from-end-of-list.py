# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next
        if count == n:
            return head.next
        
        curr = head
        for i in range(count-n-1):
            curr = curr.next
            
        temp = curr.next
        curr.next = temp.next
        temp.next = None
        
        return head
            
        