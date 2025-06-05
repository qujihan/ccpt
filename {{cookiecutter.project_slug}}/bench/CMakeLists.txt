find_package(benchmark REQUIRED)
file(GLOB BENCH_SRC ${CMAKE_CURRENT_SOURCE_DIR}/*.cc)
foreach(bench_file ${BENCH_SRC})
    get_filename_component(bench_file_name ${bench_file} NAME_WE)
    add_executable(${bench_file_name} ${bench_file}) 
    target_link_libraries(${bench_file_name} PRIVATE benchmark::benchmark_main ${PROJECT_NAME})
endforeach()

