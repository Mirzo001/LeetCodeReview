# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        #creating a dummy node
    
        dummy = curr = ListNode(0) # curr is the curr pointer for our DUMMY

        while l1 and l2:
            if l1.val<l2.val:
                curr.next = l1
                l1 = l1.next

            else:
                curr.next = l2
                l2 = l2.next

            curr = curr.next

            # now we 'll see if there are still some elements left then we ll add them as well
        if l1: curr.next = l1

        if l2 : curr.next = l2

        return dummy.next
l1 = [2,5,6,3,1]
l2 = [33,62,1,3,6]
test = Solution()
test.mergeTwoLists(l1, l2)