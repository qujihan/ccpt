cmake_minimum_required(VERSION 4.0.0)

project(
    {{ cookiecutter.project_slug }}
    VERSION 1.0.0
    LANGUAGES CXX
)  

set(CMAKE_EXPORT_COMPILE_COMMANDS ON)
set(CMAKE_BUILD_TYPE {{ cookiecutter.build_type }})
set(CMAKE_CXX_STANDARD {{ cookiecutter.cxx_minimum_standard }})
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(ENABLE_BUILD_TESTS ON CACHE BOOL "Build tests")
set(ENABLE_BUILD_BENCHMARKS ON CACHE BOOL "Build benchmark")

# Lib
add_library(
    ${PROJECT_NAME} STATIC
    ${CMAKE_CURRENT_SOURCE_DIR}/src/add.cc
)
target_include_directories(
    ${PROJECT_NAME} PUBLIC
    ${CMAKE_CURRENT_SOURCE_DIR}/include
)
add_library( ${PROJECT_NAME}::${PROJECT_NAME} ALIAS ${PROJECT_NAME})

# Main
add_executable(main main.cc)
target_link_libraries(main PRIVATE ${PROJECT_NAME})
target_include_directories(main PRIVATE ${CMAKE_CURRENT_SOURCE_DIR}/include)

# Test
if(ENABLE_BUILD_TESTS)
    add_subdirectory(tests)
endif()

# Benchmark
if(ENABLE_BUILD_BENCHMARKS)
    add_subdirectory(bench)
endif()
