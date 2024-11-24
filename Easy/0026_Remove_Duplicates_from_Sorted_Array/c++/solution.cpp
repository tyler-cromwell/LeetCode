class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int length = nums.size();
        
        if (nums.size() == 0) {
            return 0;
        }
        
        for (int i = 0; i < nums.size()-1;) {
            if (nums[i] == nums[i+1]) {
                nums.erase(nums.begin()+i);
                length--;
            } else {
                i++;
            }
        }
        
        return length;
    }
};
