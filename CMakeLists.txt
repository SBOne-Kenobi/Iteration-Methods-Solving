cmake_minimum_required(VERSION 3.10)
project(iteration)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_FLAGS "-Wall -Wextra -Werror")

include_directories(include)

add_executable(iteration src/main.cpp
        include/Matrix.h include/Matrix_impl.inl
        include/ArithmeticRestriction.h
        include/IterationMethod.h include/SimpleIterationMethod.h)
