cmake_minimum_required(VERSION 3.25)
project(cpp_yandex)

set(CMAKE_CXX_STANDARD 17)

# add_executable(cpp_yandex _31_1_print.cpp)
add_executable(cpp_yandex _43_b.cpp)

target_include_directories(cpp_yandex PRIVATE ${CMAKE_CURRENT_SOURCE_DIR}/util/)