class TreeNode(object):
    def __init__(self, val_data = None):
        self.val = val_data
        self.left = None
        self.right = None
    
    def printVal(self):
        print(self.val)


def dfs_recursive(root: TreeNode):
    if (not root):
        return
    
    root.printVal()
    dfs_recursive(root.left)
    dfs_recursive(root.right)


        