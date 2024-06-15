/**
 * _0205_isomorphic_strings
 * https://leetcode.com/problems/isomorphic-strings
 * 
 * TODO:
 * - Implement w/o hashmap with two char map[128] arrays
*/

#include <iostream>
#include <string>

using namespace std;

class Solution {

/**
 * Solution
 * 
 * Complexity:
 *     time: O(n)
 *     memory: O(n)
*/
        
public:
    bool isIsomorphic(string s, string t) {

        unordered_map<char, char> map_s_t = {};
        unordered_map<char, char> map_t_s = {};

        for (size_t i = 0; i < s.size(); ++i) {
            if (map_s_t.find(s[i]) != map_s_t.end()) {
                if (map_s_t[s[i]] != t[i]) {
                    return false;
                }
            } else if (map_t_s.find(t[i]) != map_t_s.end()) {
                if (map_t_s[t[i]] != s[i]) {
                    return false;
                }
            } else {
                map_s_t[s[i]] = t[i];
                map_t_s[t[i]] = s[i];
            }
        }

        return true;     
    }
};


int main() {

    auto solution = make_shared<Solution>();

    string s = "eggea";
    string t = "baaba";

    cout << "s: " << s << endl;
    cout << "t: " << t << endl;

    auto result = solution->isIsomorphic(s, t);

    cout << "result: " << result << endl;

    return 0;
}