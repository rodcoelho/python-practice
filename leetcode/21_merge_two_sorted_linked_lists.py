"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. 

The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
"""

import unittest
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged_list = None
        current_merged_list = None

        l1_next_is_none = False if list1 is not None else True
        l2_next_is_none = False if list2 is not None else True

        current_l1 = list1
        current_l2 = list2
        while not l1_next_is_none or not l2_next_is_none:
            
            current_l1_val = current_l1.val if current_l1 is not None else None
            current_l2_val = current_l2.val if current_l2 is not None else None

            if current_l1_val is not None and (l2_next_is_none or current_l1_val <= current_l2_val):
                # add to merged
                if merged_list is None:
                    merged_list = ListNode(val=current_l1_val, next=None)
                    current_merged_list = merged_list
                else:
                    new_node_merged_list = ListNode(val=current_l1_val, next=None)
                    current_merged_list.next = new_node_merged_list
                    current_merged_list = new_node_merged_list
                
                # move to next in list
                current_l1 = current_l1.next
                 
            elif current_l2_val is not None and (l1_next_is_none or current_l1_val >= current_l2_val):
                # add to merged
                if merged_list is None:
                    merged_list = ListNode(val=current_l2_val, next=None)
                    current_merged_list = merged_list
                else:
                    new_node_merged_list = ListNode(val=current_l2_val, next=None)
                    current_merged_list.next = new_node_merged_list
                    current_merged_list = new_node_merged_list
                
                # move to next in list
                current_l2 = current_l2.next

            if current_l1 is None:
                l1_next_is_none = True
            if current_l2 is None:
                l2_next_is_none = True


        return merged_list


class TestSolution(unittest.TestCase):
    def makeLinkedList(self, l: List) -> Optional[ListNode]:
        head = None
        current = None

        for ele in l:
            if head is None:
                head = ListNode(val=ele, next=None)
                current = head
            else:
                new_node = ListNode(val=ele, next=None)
                current.next = new_node
                current = new_node
        
        return head

    def makeLinkedListToList(self, ll: Optional[ListNode]) -> List:
        l = []

        if ll is None:
            return []

        next_is_none = False
        current = None
        while not next_is_none:
            if current is None:
                l.append(ll.val)
                current = ll.next
            else:
                l.append(current.val)
                current = current.next

            if current is None or current.next == None:
                next_is_none = True

        if current is not None:
            l.append(current.val)

        return l

    def testMergeTwoLists(self):
        s = Solution()

        list1 = [1,2,4]
        ll1 = self.makeLinkedList(list1)
        list2 = [1,3,4]
        ll2 = self.makeLinkedList(list2)
        expected = [1,1,2,3,4,4]
        actual = s.mergeTwoLists(ll1, ll2)
        actual_to_list = self.makeLinkedListToList(actual)
        self.assertEqual(actual_to_list, expected)

        list1 = []
        ll1 = self.makeLinkedList(list1)
        list2 = []
        ll2 = self.makeLinkedList(list2)
        expected = []
        actual = s.mergeTwoLists(ll1, ll2)
        actual_to_list = self.makeLinkedListToList(actual)
        self.assertEqual(actual_to_list, expected)

        list1 = []
        ll1 = self.makeLinkedList(list1)
        list2 = [0]
        ll2 = self.makeLinkedList(list2)
        expected = [0]
        actual = s.mergeTwoLists(ll1, ll2)
        actual_to_list = self.makeLinkedListToList(actual)
        self.assertEqual(actual_to_list, expected)



unittest.main()