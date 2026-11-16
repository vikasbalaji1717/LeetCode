
class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        while (root != nullptr) {
            // Both nodes are in the left subtree
            if (p->val < root->val && q->val < root->val) {
                root = root->left;
            }
            // Both nodes are in the right subtree
            else if (p->val > root->val && q->val > root->val) {
                root = root->right;
            }
            // Nodes split here, or root is one of the nodes
            else {
                return root;
            }
        }

        return nullptr;
    }
};
