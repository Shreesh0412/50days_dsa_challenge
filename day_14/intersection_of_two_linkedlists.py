# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        a=headA
        b=headB
        c=0
        while True:
            if a==b:
                return a 
            a=a.next
            b=b.next
            if b==None:
                c+=1
                b=headA
            if a==None:
                a=headB
            if c>1:
                return None
