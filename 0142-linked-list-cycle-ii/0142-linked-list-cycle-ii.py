class Solution(object):
    def detectCycle(self, head):
        if not head or not head.next:
            return None
        
        slow = fast = head
        
        # Step 1: Detect cycle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                break
        else:
            return None   # ✅ Only return if loop finishes normally
        
        # Step 2: Find start of cycle
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        
        return slow