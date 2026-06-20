# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        curr=head
        a=0
        while curr:
            a+=1
            curr=curr.next
        if a==n:
            return head.next
        b=a-n-1
        curr=head
        for i in range(b):
            curr=curr.next
        curr.next=curr.next.next
        return head
