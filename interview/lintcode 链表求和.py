# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 17:17:28 2017

@author: ice-fire
"""

class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    # @param l1: the first list
    # @param l2: the second list 
    # @return: the sum list of l1 and l2 
#    def addLists(self, l1, l2):
#        # write your code here
#        if l1 is None: return l2
#        if l2 is None: return l1
#        
#        flag = 0
#        while l1.next is not None or l2.next is not None:
#            if l1.next is None:
#                l1.next = ListNode(0)
#            if l2.next is None:
#                l2.next = ListNode(0)
#            
#            sumNum = l1.val + l2.val
#            if sumNum >= 10:
#                l1.val = sumNum%10
#                flag = 1
#                l1.next.val += 1
#            else:
#                l1.val = sumNum
#                flag = 0
#            l1 = l1.next
#            l2 = l2.next
#        else:
#            l1.val = l1.val + l2.val
#            if l1.val >= 10:
#                l1.val = l1.val%10
#                l1.next = ListNode(1)
#        return l1
    def addLists(self, l1, l2):
        # write your code here
        if l1 is None: return l2
        if l2 is None: return l1
         
        head1 = l1
        head2 = l2         
        while head1.next is not None or head2.next is not None:
            # 存在某一链表next为空时，构造next.val = 0，不影响加法结果
            if head1.next is None:
                head1.next = ListNode(0)
            if head2.next is None:
                head2.next = ListNode(0)
            sumNum = head1.val + head2.val
            if sumNum >= 10:
                head1.val = sumNum%10
                head1.next.val += 1
            else:
                head1.val = sumNum    
            head1 = head1.next
            head2 = head2.next
        else:
            # 链表末尾时，单独处理，其和大于10时，追加节点
            head1.val = head1.val + head2.val
            if head1.val >= 10:
                head1.val = head1.val%10
                head1.next = ListNode(1)
        return l1


