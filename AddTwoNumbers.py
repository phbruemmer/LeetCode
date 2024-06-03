class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        def linked_list(node):
            print(node)
            output = ListNode(node)
        val1 = l1
        val2 = l2

        remainder = 0

        while val1:
            out = val1.val + val2.val
            linked_list(out)
            val1 = val1.next
            val2 = val2.next


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

solution_instance = Solution()
sol = solution_instance.addTwoNumbers(l1, l2)
