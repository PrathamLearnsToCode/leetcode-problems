/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        ListNode* temp1 = headA;
        ListNode* temp2 = headB;
        unordered_set<ListNode*> nodeSet;
        while(temp1){
            nodeSet.insert(temp1);
            temp1 = temp1->next;
        }
        while(temp2){
            if(nodeSet.find(temp2) != nodeSet.end()){
                return temp2;
            }
            temp2 = temp2->next;
        }

        return nullptr;
    }
};
