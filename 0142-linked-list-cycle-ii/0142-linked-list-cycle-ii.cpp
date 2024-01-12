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
    ListNode *detectCycle(ListNode *head) {
        if(head == NULL){
            return NULL;
        }

        ListNode *s = head;
        ListNode *f = head;
        bool loop = false;

        while(f!=NULL){
            f = f->next;
            if(f!=NULL){
                f = f->next;
                s = s->next;
            }

            if(f == s){
                s = head;
                while(s!=f){
                    s = s->next;
                    f = f->next;
                }
                return s;
            }
        }


        return NULL;
    }
};