cmake_minimum_required(VERSION 3.27)
project(c C)

set(CMAKE_C_STANDARD 11)

include_directories(.)

add_executable(c
        calckey.c)
