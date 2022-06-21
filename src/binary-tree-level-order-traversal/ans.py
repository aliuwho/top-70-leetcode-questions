# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        vals = []
        nodes = [(root, 0)]

        while len(nodes) > 0:
            currNode = nodes.pop(0)
            currRoot = currNode[0]
            currLevel = currNode[1]
            if currRoot == None:
                continue

            if len(vals) <= currNode[1]:
                vals.append([currRoot.val])
            else:
                vals[currLevel].append(currRoot.val)
            nodes.append((currRoot.left, currLevel + 1))
            nodes.append((currRoot.right, currLevel + 1))

        return vals
