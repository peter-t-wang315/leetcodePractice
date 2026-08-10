/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
public class Solution {
    public List<int> InorderTraversal(TreeNode root) {
        return (helper(root));
    }

    public List<int> helper(TreeNode node) {
        List<int> ret = new();
        if (node == null) {
            return ret;
        }
        if (node.left != null) {
            ret = helper(node.left);
        }
        ret.Add(node.val);
        if(node.right != null) {
            ret.AddRange(helper(node.right));
        }
        return ret;
    }
}