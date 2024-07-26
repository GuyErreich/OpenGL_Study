cmake_minimum_required(VERSION 3.15)
project(MyOpenGLProject)

find_package(glfw3 REQUIRED)
find_package(OpenGL REQUIRED)
find_package(stb REQUIRED)
find_package(Catch2 REQUIRED)

include_directories (${CMAKE_SOURCE_DIR}/include)

file(GLOB_RECURSE SOURCES ${CMAKE_SOURCE_DIR}/src/*.cpp ${CMAKE_SOURCE_DIR}/src/*.c)
add_executable(MyOpenGLProject ${SOURCES})
target_link_libraries(MyOpenGLProject glfw OpenGL::GL stb::stb)

include_directories (${CMAKE_SOURCE_DIR}/tests)

# Set the C++ standard for Catch2 separately
file(GLOB_RECURSE TESTS ${CMAKE_SOURCE_DIR}/tests/*.cpp ${CMAKE_SOURCE_DIR}/src/*.cpp ${CMAKE_SOURCE_DIR}/src/*.c)
list(REMOVE_ITEM TESTS ${CMAKE_SOURCE_DIR}/src/main.cpp)
add_executable(tests ${TESTS})
target_link_libraries(tests glfw OpenGL::GL stb::stb Catch2::Catch2WithMain)