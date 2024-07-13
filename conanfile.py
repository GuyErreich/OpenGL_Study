import os
from conan import ConanFile
from conan.tools.cmake import CMake, CMakeToolchain, CMakeDeps, cmake_layout
from conan.tools.files import copy

class MyOpenGLProject(ConanFile):
    name = "my_opengl_project"
    version = "1.0"
    # license = "MIT"
    # author = "Your Name <you@example.com>"
    # url = "https://github.com/your/repo"
    description = "My OpenGL Project"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = {"shared": False}
    generators = "CMakeToolchain"

    def requirements(self):
        self.requires("glfw/3.4")
        self.requires("opengl/system")
        self.requires("stb/cci.20240213")

    def build_requirements(self):
        if self.settings.os != "Windows":
            self.tool_requires('cmake/3.29.6')

    def layout(self):
        cmake_layout(self)

    def generate(self):
        deps = CMakeDeps(self)
        deps.set_property("opengl", "cmake_file_name", "OpenGL")
        deps.set_property("opengl", "cmake_target_name", "OpenGL::GL")
        deps.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure(variables = {"CMAKE_EXPORT_COMPILE_COMMANDS": "ON"})
        cmake.build(cli_args=["--clean-first"])