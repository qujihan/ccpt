file(GLOB SRC_FILES ${CMAKE_CURRENT_SOURCE_DIR}/*.cc)
add_library(src_objs ${SRC_FILES})
target_include_directories(src_objs PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})