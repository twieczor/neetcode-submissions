# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    min = None
    max = None
    anc = None

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        self.min = p.val
        self.max = q.val

        if p.val == q.val:
            self.anc = p
            return
        elif q.val < p.val:
            self.min = q.val
            self.max = p.val 

        def recursive(self, node: TreeNode, p: TreeNode, q: TreeNode):
            
            if self.anc is not None:
                return

            if node is None:
                return

            #print(node.val)

            if node.val > self.max:
                recursive(self, node.left, p, q)
            elif node.val < self.min:
                recursive(self, node.right, p, q)
            else:
                self.anc = node
                return

        recursive(self, root, p, q)
        return self.anc


        i

