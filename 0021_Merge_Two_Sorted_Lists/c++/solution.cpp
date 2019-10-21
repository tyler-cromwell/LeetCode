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
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode *list = new ListNode(-1);
        ListNode *ptr1 = l1;
        ListNode *ptr2 = l2;
        ListNode *start = list;
        
        while (ptr1 || ptr2) {
            if (ptr1 && !ptr2) {
                list->next = new ListNode(ptr1->val);
                ptr1 = ptr1->next;
            }
            else if (!ptr1 && ptr2) {
                list->next = new ListNode(ptr2->val);
                ptr2 = ptr2->next;
            }
            else {
                if (ptr1->val <= ptr2->val) {
                    list->next = new ListNode(ptr1->val);
                    ptr1 = ptr1->next;
                }
                else {
                    list->next = new ListNode(ptr2->val);
                    ptr2 = ptr2->next;
                }
            }
            
            list = list->next;
        }

        ListNode* ret = start->next;
        delete start;
        return ret;
    }
};
