"""
Explanations here:

1-2-3-4-5
k = 2
5-1-2-3-4
k = 1
4-5-1-2-3
k = 0

Steps
1. find last, store value
2. point last to first
3. iterate k times
4. point forlast to null

Ohhhh we need to find the length of the list
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
      def find_last(head):
        n = 0
        while head.next:
          n += 1
          head = head.next
        return n, head
      
      n, old_last = find_last(head)
      old_head = head
      
      k = k%n
      counter = n
      while head.next:
        if counter-1 == k:
          new_last = head
          new_head = head.next
          break
        count -= 1
        
      new_last.next = None
      new_head.next = old_head
      
      return new_head
      
      # def findLast(head):
      #   n = 0
      #   while head.next != None:
      #     ptr = head.next
      #     n += 1
      #   return n, ptr
    
      # def findForeLast(head, n):
      #   while n >= 2:
      #     ptr = head.next
      #     n-1
      #   return ptr
      
      # n, last = findLast(head)
      # k = k%n
      # while k > 0:
      #   n, last = findLast(head)
      #   forelast = findForLast(head, n)
      #   last.next, forelast.next = head, None
      #   k -= 1        
          