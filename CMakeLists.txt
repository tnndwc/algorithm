cmake_minimum_required(VERSION 3.3)
project(algorithm)

set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -Wall -Werror")

set(SOURCE_FILES
        #string_manacher.c
        string_findmin.c random_util.h random_util.c insert_sort.c insert_sort.h)
add_executable(algorithm ${SOURCE_FILES})