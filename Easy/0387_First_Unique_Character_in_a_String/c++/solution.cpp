class Solution {
public:
    int firstUniqChar(string s) {
        /*
         * O(n) / O(n) solution: Hash Map
         */
        map<char,int> counts;
        
        for (int i = 0; i < s.size(); i++) {
            char c = s.at(i);
            pair<map<char,int>::iterator,bool> ret;
            ret = counts.insert( pair<char,int>(c,1) );

            if (ret.second == false) {
                ret.first->second++;
            }
        }
        
        for (int i = 0; i < s.size(); i++) {
            int value = counts.find(s.at(i))->second;

            if (value == 1) {
                return i;
            }
        }
        
        return -1;
    }
};
