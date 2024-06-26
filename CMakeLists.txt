cmake_minimum_required(VERSION 3.15)
project(MyOpenGLProject)

# find_package(glfw REQUIRED)
add_subdirectory(glfw-3.4)

find_package(OpenGL REQUIRED)

add_executable(my_project main.cpp)

target_link_libraries(my_project PRIVATE glfw OpenGL::GL)