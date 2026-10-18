class Solution(object):
    def isPalindrome(self, head):
        value = []
        curr = head
        while curr:
            value.append(curr.val)
            curr = curr.next

        if value == value[::-1]:
            return True

        else:
            return False
