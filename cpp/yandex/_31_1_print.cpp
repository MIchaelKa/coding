
#include <iostream>
#include <fstream>

using namespace std;

template <typename Container>
void Print1(const Container& container, const string& sep) {
    if (container.size() == 0) {
        return;
    }
    auto iter = container.begin();
    for (; iter != container.end()-1; ++iter) {
        cout << *iter << sep;
    }
    cout << *iter << endl;
}

template <typename Container>
void Print2(const Container& container, const string& sep) {
    if (container.size() == 0) {
        return;
    }
    auto iter = container.begin();
    for (; iter != --container.end(); ++iter) {
        cout << *iter << sep;
    }
    cout << *iter << endl;
}

template <typename Container>
void Print(const Container& container, const string& sep) {
    bool first = true;
 
    for (const auto& elem : container) {
        if (!first) {
            std::cout << sep;
        } else {
            first = false;
        }
 
        std::cout << elem;
    }
 
    std::cout << "\n";
}

int main() {

    cout << "_31_1_print" << endl;

    vector<int> vec = {1, 2, 3, 4, 5};
    // vector<int> vec;
    Print(vec, ", ");

    return 0;
}

