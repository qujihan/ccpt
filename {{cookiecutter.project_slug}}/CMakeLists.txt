cmake_minimum_required(VERSION 4.0.0)

project(
    {{ cookiecutter.project_slug }}
    VERSION 1.0.0
    LANGUAGES CXX
)  

set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

set(CMAKE_CXX_STANDARD {{ cookiecutter.cxx_minimum_standard }})
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Libs
# include(cmake/xxx.cmake)
# list(APPEND EXTERNAL_LIBS xxx)

# Src Dir
add_subdirectory(src)

# Main
add_executable(main main.cc)
target_link_libraries(main PRIVATE src_objs ${EXTERNAL_LIBS})

# Unittest
include(cmake/gtest.cmake)
file(GLOB_RECURSE TESTS_SRCS tests/*.cc)
add_executable(unittest ${TESTS_SRCS})
target_include_directories(unittest PRIVATE tests)
target_link_libraries(unittest PRIVATE src_objs gtest_main gmock ${EXTERNAL_LIBS})
