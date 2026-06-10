# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        pList1 = list1
        pList2 = list2
        phead = None
        ans = None
        mini = None

        while pList1 != None and pList2 != None:
            if pList1.val < pList2.val:
                mini = pList1.val
                pList1 = pList1.next
            else:
                mini = pList2.val
                pList2 = pList2.next
            if ans == None:
                ans = ListNode(mini)
                phead = ans
            else:
                phead.next = ListNode(mini)
                phead = phead.next

        if ans == None:
            return pList1 if pList1 != None else pList2

        while pList1 != None:
            phead.next = pList1
            break

        while pList2 != None:
            phead.next = pList2
            break

        return ans