#include <iostream>
#include <vector>


float solution(const std::vector<std::vector<float>>& intervals) {

    float low = 0;
    float high = 0;

    // intervals -> intermidiate

    std::vector<std::tuple<float, bool>> points;

    for (const auto& interval : intervals) {
        points.push_back({interval[0], true});
        points.push_back({interval[1], false});
    }

    std::sort(points.begin(), points.end(), [](const std::tuple<float, bool>& t1,
                                                const std::tuple<float, bool>& t2){
                                                    return t1[0] < t2[0];
    })

    


}

int main() {
    // you can write to stdout for debugging purposes, e.g.
    std::cout << "This is a debug message" << std::endl;

    std::vector<std::vector<float>> intervals;

    return 0;
}
