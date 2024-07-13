cmake_minimum_required(VERSION 3.15)
project(MyOpenGLProject)

find_package(glfw3 REQUIRED)
find_package(OpenGL REQUIRED)
find_package(stb)

include_directories (${CMAKE_SOURCE_DIR}/include)

file(GLOB_RECURSE SOURCES ${CMAKE_SOURCE_DIR}/src/*.cpp ${CMAKE_SOURCE_DIR}/src/*.c)

add_executable(MyOpenGLProject ${SOURCES})

target_link_libraries(MyOpenGLProject glfw OpenGL::GL stb::stb)