import os
from conan import ConanFile
from conan.tools.cmake import CMake, CMakeToolchain, CMakeDeps, cmake_layout
from conan.tools.build import build_jobs
from conan.tools.files import copy, get, mkdir, rmdir
from conan.tools.system import package_manager
from conan.tools.system.package_manager import Apt

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
    # generators = "CMakeDeps", "CMakeToolchain"
    generators = "CMakeToolchain"
    exports_sources = "*"

    def requirements(self):
        mkdir(self, 'extensions')
        get(self, "https://github.com/glfw/glfw/archive/refs/tags/3.4.tar.gz", destination='extensions')
    #     self.requires("glfw/3.4")

    def system_requirements(self):
        Apt(self).install(["libwayland-dev", "pkg-config", "libxkbcommon-dev", "xorg-dev"],True,True)
        # if self.settings.os == "Windows":
        #     self.build_requires("pkg_config_installer/0.29.2@bincrafters/stable")

    def layout(self):
        cmake_layout(self)

    def build(self):
        cmake = CMake(self)
        cmake.configure(build_script_folder="extensions/glfw-3.4")
        cmake.build(cli_args=["--clean-first"])
        # cmake.configure()
        

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["glfw"]