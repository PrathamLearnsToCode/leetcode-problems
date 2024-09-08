# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reversed(self, head: Optional[ListNode]) -> int:
        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            
        return prev
        
        
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        second_half = self.reversed(slow)
        max_sum = 0
        first_half = head
        while second_half:
            twin_sum = first_half.val + second_half.val
            max_sum = max(max_sum, twin_sum)
            first_half = first_half.next
            second_half = second_half.next
            
        return max_sum
        
        