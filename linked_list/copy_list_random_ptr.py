"""
A linked list of length n is given such that each node contains an additional random pointer,
which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes,
where each new node has its value set to the value of its corresponding original node. Both the next
and random pointer of the new nodes should point to new nodes in the copied list such that the pointers
in the original list and copied list represent the same list state. None of the pointers in the new list
should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding
two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index]
where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
Your code will only be given the head of the original linked list.
"""
from typing import Optional
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
class Solution:

    def _print_list(self, head):
        node = head
        count = 0
        while node:
            print("count:", count)
            print("val:",node.val)
            if node.random is None:
                print("random:", None)
            else:
                print("random:", node.random)
            count += 1
            node = node.next

    def _wire_randoms(self, head):
        nodes = []
        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next

        #reassign each .random exactly once
        for idx, node in enumerate(nodes):
            raw = node.random
            if isinstance(raw, int) and 0 <= raw < len(nodes):
                node.random = nodes[raw]
                #node.random = nodes[node.random]
            else:
                node.random = None
        return head

    def _build_list(self, input):
        if not input:
            return None
        head = Node(x=input[0][0], next=None, random=input[0][1])
        prev = head
        for val, rnd_idx in input[1:]:
            new_node = Node(x=val,next=None,random=rnd_idx)
            prev.next = new_node
            prev = new_node
        head = self._wire_randoms(head)
        return head

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # put nodes in list
        nodes = []
        node_map = {}
        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next
        node_map = {}
        for node in nodes:
            if node.random == None:
                node_map[node] = None
            else:
                node_map[node] = nodes.index(node.random)
        # make list of copied nodes
        new_nodes = []
        for node in nodes:
            new_node = Node(node.val) # copy node
            new_nodes.append(new_node) # put in new node list
        # take second pass over nodes and wire randoms in copied node list
        for idx, node in enumerate(nodes):
            ran_idx = node_map[node] # get the index of this node's random
            if ran_idx is None:
                new_nodes[idx].random = None
            else:
                new_nodes[idx].random = new_nodes[ran_idx] # assign the copied node's random to the node at this node's random index
            if idx == len(nodes) - 1:
                new_nodes[idx].next = None
            else:
                new_nodes[idx].next = new_nodes[idx+1]  

        return new_nodes[0]     

if __name__ == "__main__":
    input = [[7,None],[13,0],[11,4],[10,2],[1,0]]
    solution = Solution()
    head = solution._build_list(input)
    solution.copyRandomList(head)