import sys
sys.path.append("..")
from base_class.tree_node import TreeNode, dfs_recursive
from collections import deque as deque

def bfs_with_mark(k: int, root: TreeNode):
    q = deque([root])
    step = 0
    ans = []
    while q:
        size = len(q)
        for _ in range(size):
            node = q.popleft()
            if (step == k):
                ans.append(node)
            if (node.right):
                q.append(node.right)
            if (node.left):
                q.append(node.left)
        step += 1
    return ans

# dfs by recursion
def dfs_path_total(root: TreeNode, path = None, ans = None):
    if not root:
        return
    if not root.left and root.right:
        return
    path.append(root)
    dfs_path_total(root.left)
    dfs_path_total(root.right)
    return

if __name__ == "__main__":
    # 1st floor
    root = TreeNode(1)
    # 2nd floor
    f2_01 = TreeNode(2)
    root.left = f2_01
    f2_02 = TreeNode(3)
    root.right = f2_02
    # 3rd floor
    f3_01 = TreeNode(4)
    f3_02 = TreeNode(5)
    f3_03 = TreeNode(6)
    f2_01.left = f3_01
    f2_01.right = f3_02
    f2_02.right = f3_03
    dfs_recursive(root)
    


    
