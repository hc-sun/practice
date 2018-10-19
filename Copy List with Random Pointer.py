# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):    
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """ 
        if not head:
            return None
        cur = head
        dic = {}
        while cur: #create nodes
            node = RandomListNode(cur.label)
            dic[cur] = node
            cur = cur.next
        cur = head
        while cur: #create pointer, if not exist
            dic[cur].next = dic.get(cur.next) #Return the value of dic if key is in the dic else None
            dic[cur].random = dic.get(cur.random)
            cur = cur.next
        return dic.get(head)
# A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.
# Return a deep copy of the list.