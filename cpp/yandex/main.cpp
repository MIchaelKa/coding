
#include <iostream>
#include <fstream>

using namespace std;

int main() {
    cout << "_31_1_print" << endl;

    vector<int> vec;
    vector<string> text;

    string line;
    // ifstream in("input.txt");
    ifstream in("/Users/user006/Developer/projects_my/coding/cpp/yandex/input.txt");
    
    // Check if the file is successfully opened 
    if (!in.is_open()) { 
        cerr << "Error opening the file!" << endl; 
        return 1; 
    } 

    while(getline(in,line) && !line.empty()){
        vec.push_back(stoi(line));
        text.push_back(line);
    }

    // for (const auto& t : text) {
    //     cout << t << endl;
    // }

    return 0;
}

int main() {

    vector<int> vec;

    string line;
    ifstream in("input.txt");

    while(getline(in,line) && !line.empty()){
        vec.push_back(stoi(line));
    }

    return 0;
}