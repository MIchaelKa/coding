
#include <iostream>
#include <string>

using namespace std;

class Solution {
public:
    bool isIsomorphic(string s, string t) {


        return true;     
    }
};


int main() {

    auto solution = make_shared<Solution>();

    string s = "egg";
    string t = "add";

    cout << "s: " << s << endl;
    cout << "t: " << t << endl;

    auto result = solution->isIsomorphic(s, t);

    cout << "result: " << result << endl;

    return 0;
}