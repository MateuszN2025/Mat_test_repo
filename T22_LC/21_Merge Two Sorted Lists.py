from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()   # placeholder node, result list starts after it
        current = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        # attach whichever list still has nodes left
        current.next = list1 or list2

        return dummy.next  # skip the placeholder, return real head


# --- manual test (no framework needed) ---

def make_list(values: list[int]) -> Optional[ListNode]:
    dummy = ListNode()
    cur = dummy
    for v in values:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


def to_python_list(head: Optional[ListNode]) -> list[int]:
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


s = Solution()
head = s.mergeTwoLists(make_list([1, 2, 4]), make_list([1, 3, 4]))
print(to_python_list(head))  # [1, 1, 2, 3, 4, 4]
