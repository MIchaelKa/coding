/**
 * _0151_reverse_words_in_str.cpp
 * https://leetcode.com/problems/reverse-words-in-a-string
 * 
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
    string reverseWords(string s) {

        string res;
        res.reserve(s.size());
        int position = 0;

        for (auto const& c : s) {
            if (c == ' ') {
                position = 0;
            } else {
                if (position == 0 && !res.empty() && res[0] != ' ') {
                    res.insert(0, 1, ' ');
                }
                res.insert(position++, 1, c);
            }
        }
        return res;    
    }
};


int main() {

    auto solution = make_shared<Solution>();

    string s = "  the sky is   blue   ";

    cout << "s: " << s << endl;

    auto result = solution->reverseWords(s);

    cout << "r: " << result << endl;

    return 0;
}