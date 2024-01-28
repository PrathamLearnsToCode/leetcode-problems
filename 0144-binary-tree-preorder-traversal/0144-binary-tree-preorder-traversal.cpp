/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<int> preorderTraversal(TreeNode* root) {
        vector <int> nodeVec;
        doTraversal(nodeVec,root);
        return nodeVec;
    }
    void doTraversal(vector<int> &nodeVec, TreeNode* temp)
    {
        if(temp==nullptr)
            return;
        nodeVec.push_back(temp->val);
        doTraversal(nodeVec,temp->left);
        doTraversal(nodeVec,temp->right);
    }
};