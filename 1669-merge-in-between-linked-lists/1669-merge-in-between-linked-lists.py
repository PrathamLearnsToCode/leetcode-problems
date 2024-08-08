class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        # Step 1: Find the node just before the ath node
        prev_a = list1
        for _ in range(a - 1):
            prev_a = prev_a.next
        
        # Step 2: Find the node just after the bth node
        after_b = prev_a
        for _ in range(b - a + 2):
            after_b = after_b.next
        
        # Step 3: Connect the end of list2 to after_b
        curr = list2
        while curr.next:
            curr = curr.next
        curr.next = after_b
        
        # Step 4: Connect prev_a to the head of list2
        prev_a.next = list2
        
        return list1