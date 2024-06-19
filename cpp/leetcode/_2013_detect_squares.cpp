/**
 * _2013_detect_squares.cpp
 * https://leetcode.com/problems/detect-squares
*/

#include <iostream>
#include <string>
#include <vector>

using namespace std;

class DetectSquares {

private:
    unordered_map<int, vector<int>> x2y;
    unordered_map<int, vector<int>> y2x;

public:
    DetectSquares() {
        
    }
    
    void add(vector<int> point) {
        x2y[point[0]].push_back(point[1]);
        y2x[point[1]].push_back(point[0]);
    }
    
    int count(vector<int> point) {

        int x_find = point[0];
        int y_find = point[1];
    
        if (y2x.find(y_find) == y2x.end()) {
            return 0;
        }

        if (x2y.find(x_find) == x2y.end()) {
            return 0;
        }

        int count = 0;
        auto xs = y2x[y_find];
        
        for (int x : xs) {
            int side_len = std::abs(x - x_find);

            if (side_len == 0) {
                continue;
            }

            for (int y : {y_find + side_len, y_find - side_len}) {
                auto ys_1 = x2y[x_find];
                int count_corner_1 = std::count(ys_1.begin(), ys_1.end(), y);

                auto ys_2 = x2y[x];
                int count_corner_2 = std::count(ys_2.begin(), ys_2.end(), y);

                count += count_corner_1 * count_corner_2;
            }
        }

        return count;
    }
};


int main() {

    auto solution = make_shared<DetectSquares>();

    // test 1

    // solution->add({3, 10});
    // solution->add({11, 2});
    // solution->add({11, 2});
    // solution->add({3, 2});
    // solution->add({3, 2});
    // auto result = solution->count({11, 10});
    // cout << "r: " << result << endl;

    // test 2

    solution->add({1, 1});
    solution->add({1, 4});

    solution->add({10, 4});
    solution->add({10, 1});
    solution->add({7, 7});

    solution->add({10, 7}); // 1
    cout << "r: " << solution->count({7, 4}) << endl;

    solution->add({7, 1});  // 2
    cout << "r: " << solution->count({7, 4}) << endl;

    solution->add({7, 1});  // 3
    cout << "r: " << solution->count({7, 4}) << endl;

    solution->add({10, 1}); // 5
    cout << "r: " << solution->count({7, 4}) << endl;

    solution->add({10, 4}); // 9
    cout << "r: " << solution->count({7, 4}) << endl;


    return 0;
}