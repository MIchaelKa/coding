
#include "logger.h"

int main() {
    Logger x1;
    Logger x2;

    x1 = x2;
    x1 = std::move(x2);

    return 0;
}