class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        /*
         * O(n^2) solution: Brute Force
         */
        vector<int> indices(2,0); 
        
        for (int i = 0; i < nums.size(); i++) {
            for (int j = 0; j < nums.size(); j++) {
                if (i == j) continue;
                
                if (nums[i] + nums[j] == target) {
                    indices[0] = i;
                    indices[1] = j;
                    return indices;
                }
            }
        }
        
        return indices;
    }
};
