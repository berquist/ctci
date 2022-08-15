cmake_minimum_required(VERSION 3.8)
project(leetcode CXX)

function(create_executable src)
    add_executable("${src}.x" "${src}.cpp")
endfunction(create_executable)

create_executable(1)
