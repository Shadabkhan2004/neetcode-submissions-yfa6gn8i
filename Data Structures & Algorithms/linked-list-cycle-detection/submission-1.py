# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        llc = {}

        temp = head

        while temp:
            if temp in llc:
                return True
            llc[temp] = 'visited'
            temp = temp.next

        return False