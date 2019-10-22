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
    bool hasCycle(ListNode *head) {
        /*
         * O(n) / O(1) solution: Slow & Fast pointers
         */
        ListNode *slow = head;
        ListNode *fast = head;
        
        if (head == NULL) {
            return false;
        }
        
        while (true) {
            if (fast->next && fast->next->next) {
                slow = slow->next;
                fast = fast->next->next;
            }
            else {
                return false;
            }
            
            if (slow == fast) {
                return true;
            }
        }
        
        return false;
    }
};
