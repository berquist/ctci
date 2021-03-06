cmake_minimum_required(VERSION 3.11)
project(ctci C CXX)

set(CMAKE_MODULE_PATH
    ${CMAKE_MODULE_PATH}
    ${CMAKE_SOURCE_DIR}/cmake
    )

set(CMAKE_CXX_STANDARD 17)

enable_testing()

find_package(GTest REQUIRED)

find_package(GoogleBenchmark REQUIRED)
include_directories(${benchmark_INCLUDE_DIRS})

set(SRC_C
    ctci/ch12.c
    )

set(SRC_CXX
    ctci/ch1.cpp
    ctci/ch12.cpp
    ctci/p131.cpp
    )

# add_executable(ctci_c.x ${SRC_C})
# add_executable(ctci_cxx.x ${SRC_CXX})

foreach(srcfilename ${SRC_C} ${SRC_CXX})
    # 1. split at path separators, take last one to get filename
    # 2. strip off extension
    # get_filename_component(directory ${srcfilename} DIRECTORY)
    # get_filename_component(name ${srcfilename} NAME)
    # get_filename_component(stub ${srcfilename} NAME_WE)
    # message(STATUS "${srcfilename} -> ${directory}/${stub}.x")
    # file(TO_NATIVE_PATH "${directory}/${stub}.x" target)
    # message(STATUS "${srcfilename} -> ${target}")
    # add_executable("${target}" "${srcfilename}")
    # add_executable("${srcfilename}.x" "${srcfilename}")
    set(replaced ${srcfilename})
    string(REPLACE "/" "_" replaced ${replaced})
    string(REPLACE "." "_" replaced ${replaced})
    # message(STATUS "${srcfilename} -> ${replaced}")
    add_executable("${replaced}.x" ${srcfilename})
    target_link_libraries("${replaced}.x" ${GTEST_BOTH_LIBRARIES} ${benchmark_LIBRARIES})
    add_test("${replaced}" "${replaced}.x")
endforeach()
