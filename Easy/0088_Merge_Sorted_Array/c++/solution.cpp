class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        int index1 = m-1;
        int index2 = n-1;
        
        for (int i = (m+n-1); i >= 0; i--) {
            if (index2 < 0) {
                break;
            }
            else if (index1 < 0) {
                nums1[i] = nums2[index2];
                index2--;
            }
            else if (nums1[index1] > nums2[index2]) {
                nums1[i] = nums1[index1];
                index1--;
            }
            else if (nums2[index2] > nums1[index1]) {
                nums1[i] = nums2[index2];
                index2--;
            }
            else {
                nums1[i] = nums1[index1];
                index1--;
            }
        }
    }
};
