# __Big O time__
# The big 0 time for this algorithm is O(n) where n is the length of the 2 trees. This is because we have to traverse each tree once to find the leaf node's values.
# That leaves us with O(2n). Then we have to compare both lists that were given back because of this and that would be O(4n). Then you simply remove the constants and
# you are left with O(n) time.

# __Space complexity__
# The space complexity of this algorithm is O(n) where n is the amount of leaf nodes for the 2 trees. This is because we create 2 arrays of each trees leaf nodes.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def findLeaves(root, treeLeaves):
    if root.left == None and root.right == None:
        treeLeaves.append(root.val)
        return

    if root.left != None:
        findLeaves(root.left, treeLeaves)
    if root.right != None:
        findLeaves(root.right, treeLeaves)


def leafSimilar(root1, root2):
    tree1Leaves = []
    tree2Leaves = []

    findLeaves(root1, tree1Leaves)
    findLeaves(root2, tree2Leaves)
    
    if tree1Leaves == tree2Leaves:
        return True
    return False


if __name__ == "__main__":
    root1 = TreeNode(3)
    root1.left = TreeNode(5)
    root1.left.left = TreeNode(6)
    root1.left.right = TreeNode(2)
    root1.left.right.left = TreeNode(7)
    root1.left.right.right = TreeNode(4)
    root1.right = TreeNode(1)
    root1.right.left = TreeNode(9)
    root1.right.right = TreeNode(8)

    root2 = TreeNode(3)
    root2.left = TreeNode(5)
    root2.left.left = TreeNode(6)
    root2.left.right = TreeNode(7)
    root2.right = TreeNode(1)
    root2.right.left = TreeNode(4)
    root2.right.right = TreeNode(2)
    root2.right.right.left = TreeNode(9)
    root2.right.right.right = TreeNode(8)

    print(leafSimilar(root1, root2))