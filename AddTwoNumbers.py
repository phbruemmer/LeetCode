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
        carry = 0
        start = ListNode(0)
        current = start

        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            carry, val = divmod(v1 + v2 + carry, 10)
            start.next = ListNode(val)
            start = start.next
        return current.next


l1 = ListNode(5)


l2 = ListNode(1)

solution_instance = Solution()
sol = solution_instance.addTwoNumbers(l1, l2)
print(sol.val)
