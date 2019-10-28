class Solution {
public:
    static bool compareInterval(vector<int> i1, vector<int> i2)  { 
        return (i1.at(0) < i2.at(0));
    }

    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        /*
         * O(n^2) / O(n): Brute force
         */

        /*
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
        */

        /*
         * O(nlog(n)) / O(n): Sorting method
         */

        if (intervals.size() == 0) {
            return {};
        }

        vector<vector<int>> list(intervals);
        sort(list.begin(), list.end(), compareInterval);

        for (int i = 0; i < list.size()-1; i++) {
            int a = list.at(i).at(0);
            int b = list.at(i).at(1);
            int c = list.at(i+1).at(0);
            int d = list.at(i+1).at(1);

            if (a >= c && b <= d) {
                list.at(i) = {-1, -1};
            }
            else if (c >= a && d <= b) {
                list.at(i+1) = list.at(i);
                list.at(i) = {-1, -1};
            }
            else if (b >= c && b <= d) {
                list.at(i+1) = {a, d};
                list.at(i) = {-1, -1};
            }
            else if (d >= a && d <= b) {
                list.at(i+1) = {c, b};
                list.at(i) = {-1, -1};
            }
        }

        vector<vector<int>> result;

        for (int i = 0; i < list.size(); i++) {
            if (list.at(i).at(0) != -1 && list.at(i).at(1) != -1) {
                result.push_back(list.at(i));
            }
        }

        return result;
    }
};
