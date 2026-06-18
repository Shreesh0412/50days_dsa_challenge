# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        a=l1
        b=l2
        d=ListNode(-1)
        curr=d
        c=0
        while a is not None or b is not None or c:
            t=c
            if a is not None:
                t+=a.val
                a=a.next
            if b is not None:
                t+=b.val
                b=b.next
            c=t//10
            t=t%10
            newNode=ListNode(t)
            curr.next=newNode
            curr=curr.next
        return d.next
