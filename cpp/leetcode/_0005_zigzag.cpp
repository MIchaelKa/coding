/**
 * _0005_zigzag
 * https://leetcode.com/problems/zigzag-conversion
 * 
 * 
*/

#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <deque>

using namespace std;

class Solution {

/**
 * deque
 * 
 * Complexity:
 *     time: O(n)
 *     memory: O(n)
*/
        
public:
    string convert(string s, int numRows) {

        if (numRows <= 1) {
            return s;
        }

        int currectSize = numRows;

        vector<deque<char>> dqs; 
        deque<char> dq;

        for (size_t i = 0; i < s.size(); ++i) {
            dq.push_back(s[i]);
            if (dq.size() == currectSize) {
                dqs.push_back(std::move(dq));
                dq = deque<char>(); 
                if (currectSize == numRows && numRows > 2) {
                    currectSize = numRows - 2;
                } else {
                    currectSize = numRows;
                }
            } 
        }

        if (!dq.empty()) {
            dqs.push_back(std::move(dq));
        }

        std::string result;
        result.reserve(s.size());
        int inc = numRows > 2 ? 2 : 1;

        for (size_t i = 0; i < dqs.size(); i += inc) {
            result += dqs[i].front();
            dqs[i].pop_front();
        }

        int leftChars = s.size() - result.size();

        while (leftChars > 0) {
            for (size_t i = 0; i < dqs.size(); ++i) {
                if (!dqs[i].empty()) {
                    if (i % 2 == 0) {
                        result += dqs[i].front();
                        dqs[i].pop_front();
                    } else {
                        result += dqs[i].back();
                        dqs[i].pop_back();
                    }
                    --leftChars;
                }
            }
        }

        return result;  
    }
};


int main() {

    auto solution = make_shared<Solution>();

    // string s = "PAYPALISHIRING";
    // int numRows = 3;
    string s = "ABCDE";
    int numRows = 4;

    cout << "s: " << s << endl;
    cout << "numRows: " << numRows << endl;

    auto result = solution->convert(s, numRows);

    cout << "r: " << result << endl;

    return 0;
}