cmake_minimum_required(VERSION 3.11)
project(ctci C CXX)

set(SRC_C
    ctci/ch12.c
    )

set(SRC_CXX
    ctci/ch12.cpp
    )

add_executable(ctci_c.x ${SRC_C})
add_executable(ctci_cxx.x ${SRC_CXX})
