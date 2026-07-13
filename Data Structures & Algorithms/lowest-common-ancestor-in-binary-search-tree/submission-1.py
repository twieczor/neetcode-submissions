# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    first = None
    anc = None
    visited = []

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        

        def find_anc(self):
            fl = len(self.first)
            sl = len(self.visited)

            print(fl, sl)


            for i in range(min(fl, sl) - 1, -1, -1):
                print(i)
                print(self.first[i].val, self.visited[i].val)
                if(self.first[i].val == self.visited[i].val):
                    print("return", self.visited[i - 1])
                    return self.visited[i]
            return None


        def preorder(self, node):
            if self.anc is not None:
                return

            if node is None:
                return

            self.visited.append(node)

            print(node.val)

            if(node.val == p.val or node.val == q.val):
                if self.first is None:
                    self.first = self.visited.copy()
                    print(self.first)
                    #self.first.append(last)
                else:
                    print("find anc")
                    self.anc = find_anc(self)
                    print(self.anc)
                    return

            preorder(self, node.left)

            preorder(self, node.right)

            self.visited.pop()

        preorder(self, root)

        print(self.anc)
        return self.anc

