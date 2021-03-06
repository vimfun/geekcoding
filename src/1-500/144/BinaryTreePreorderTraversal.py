# This help can generate a tree from array.
from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def helper(node: TreeNode, res: List[int]):
            if not node: return;
            res.append(node.val)
            helper(node.left, res)
            helper(node.right, res)
        helper(root, res)
        return res

    # 用压栈的方式求解
    def preorderTraversal2(self, root: TreeNode) -> List[int]:
        if root == None:
            return []
        stack = []
        stack.append(root)
        res = []
        while stack:
            temp = stack.pop()
            if temp:
                res.append(temp.val)
                stack.append(temp.right)
                stack.append(temp.left)
        return res

def helper(input: List, i: int) -> TreeNode:
    if i < len(input) and input[i] is not None:
        node = TreeNode(input[i])
        node.left = helper(input, i * 2 + 1)
        node.right = helper(input, i * 2 + 2)
        return node
    else:
        return None

solution = Solution()
print(solution.preorderTraversal2(helper([1,None,2, None, None, 3], 0)))