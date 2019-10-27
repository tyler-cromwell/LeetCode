class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        /*
         * O(n^2) / O(n): Brute force
         */
        if (intervals.size() == 0) {
            return {};
        }

        vector<vector<int>> temp(intervals);
        vector<vector<int>> result;

        for (int i = 0; i < temp.size()-1; i++) {
            for (int j = i+1; j < temp.size(); j++) {
                if (temp.at(j).at(0) == -1 && temp.at(j).at(1) == -1) {
                    continue;
                }
                else if (temp.at(i).at(0) >= temp.at(j).at(0) && 
                         temp.at(i).at(1) <= temp.at(j).at(1)) {
                    temp.at(i) = {-1, -1}; // temp[i] is a subset of temp[j]
                }
                else if (temp.at(j).at(0) >= temp.at(i).at(0) && 
                         temp.at(j).at(1) <= temp.at(i).at(1)) {
                    temp.at(j) = {-1, -1}; // temp[j] is a subset of temp[i]
                }
                else if (temp.at(i).at(1) >= temp.at(j).at(0) &&
                         temp.at(i).at(1) <= temp.at(j).at(1)) {
                    // temp[i] overlaps into temp[j], but not beyond
                    int start = temp.at(i).at(0);
                    int end = temp.at(j).at(1);
                    temp.at(j) = {start, end};
                    temp.at(i) = {-1, -1};
                }
                else if (temp.at(j).at(1) >= temp.at(i).at(0) &&
                         temp.at(j).at(1) <= temp.at(i).at(1)) {
                    // temp[j] overlaps into temp[i], but not beyond
                    int start = temp.at(j).at(0);
                    int end = temp.at(i).at(1);
                    temp.at(j) = {start, end};
                    temp.at(i) = {-1, -1};
                }
            }
        }

        for (int i = 0; i < temp.size(); i++) {
            if (temp.at(i).at(0) != -1 && temp.at(i).at(1) != -1) {
                result.push_back(temp.at(i));
            }
        }

        return result;
    }
};
