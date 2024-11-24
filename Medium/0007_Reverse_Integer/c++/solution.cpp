class Solution {
public:
    int reverse(int x) {
        // O(n): Convert to string, reverse, convert back to 32-bit signed int.

        std::string s1 = std::to_string(x);
        std::string s2;
        int n = s1.size();
        s2.reserve(n+1);
        
        if (s1[0] != '-') {
            for (int i = 0; i < n; i++) {
               s2[i] = s1[n-1-i];
            }
        } else {
            s2[0] = '-';
            for (int i = 1; i < n; i++) {
               s2[i] = s1[n-i];
            }
        }

        s2[n] = '\0';

        try {
            int result = std::stoi(s2, nullptr, 10);
            return result;
        } catch (std::out_of_range& e) {
            return 0;
        }
    }
};
