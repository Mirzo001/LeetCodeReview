# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Definition for iterative solution.
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Create a new linked list with references to the head and tail which are initially the same
        merged_head = merged_tail = ListNode(None)
        # While l1 and l2 both have nodes to be traversed
        while l1 and l2:
            # If the node in l1 has the smaller value
            if l1.val <= l2.val:
                # Add the node from l1 to the merged linked list
                merged_tail.next = l1
                # Move to the next node in l1
                l1 = l1.next
            # If the node in l2 has the smaller value
            else:
                # Add the node from l2 to the merged linked list
                merged_tail.next = l2
                # Move to the next node in l2
                l2 = l2.next
                
            # Update tail the tail reference to the new last node in the list
            merged_tail = merged_tail.next
        
        # At this point one of the lists has been completely traversed so attach the other one to the end of the merged linked list
        merged_tail.next = l1 or l2

        # Return the head to the merged linked list
        return merged_head.next


# Definition of recursive solution.
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # If we have not reached the end of either of the two linked lists        
        if l1 and l2:
            # If the value of the current node in l1 is larger than the current node in l2
            if l1.val > l2.val:
                # Switch the references to make sure l1 is the list with the node that has the smaller value                
                l1, l2 = l2, l1
            # Set pointer of the node with the smaller value to be the next node with the next smallest value
            l1.next = self.mergeTwoLists(l1.next, l2)
            # Retun the node with the smaller value
            return l1
        # Return the linked list of which we have not yet reached the end
        return l1 or l2