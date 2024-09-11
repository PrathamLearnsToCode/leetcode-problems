# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        temp = head
        count = 0
        while temp:
            count += 1
            temp = temp.next
        
        part_size = count//k
        remainder = count % k
        
        result = []
        current = head
        
        for i in range(k):
            part_head = current
            
            current_part_size = part_size + (1 if remainder >0 else 0)
            remainder -= 1
            
            for j in range(current_part_size - 1):
                if current:
                    current = current.next
                    
            if current:
                next_part = current.next
                current.next = None
                current = next_part
            result.append(part_head)
        return result
                
                
            
            
            
        