# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        values = []
        current = head
        while current:
            values.append(current.val)
            current = current.next
            
        max_sum = 0
        n = len(values)
        for i in range(n//2):
            twin_sum = values[i] + values[n-1-i]
            max_sum = max(max_sum, twin_sum)
            
        return max_sum