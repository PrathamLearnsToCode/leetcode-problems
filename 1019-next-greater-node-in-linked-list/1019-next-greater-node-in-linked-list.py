# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        arr = []
        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next
        
        res = [0] * len(arr)
        stack = []
        
        for i in range(len(arr)):
            while stack and arr[i] > arr[stack[-1]]:
                index = stack.pop()
                res[index] = arr[i]
            stack.append(i)
        return res
                       
                       
        