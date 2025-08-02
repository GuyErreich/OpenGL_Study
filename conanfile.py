import os
import shutil
from conan import ConanFile
from conan.tools.cmake import CMake, CMakeDeps, cmake_layout
from conan.tools.system.package_manager import Apt, Brew

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
        self.requires("glm/cci.20230113")
        self.requires("stb/cci.20240213")
        self.requires('catch2/[~3]')

    def build_requirements(self):
        if self.settings.os == "Linux":
            apt = Apt(self)
            apt.install(["cmake"], update=True)
        if self.settings.os == "Macos":
            brew = Brew(self)
            brew.install(["cmake"], update=True)

    def layout(self):
        cmake_layout(self)

    def generate(self):
        deps = CMakeDeps(self)
        deps.set_property("opengl", "cmake_file_name", "OpenGL")
        deps.set_property("opengl", "cmake_target_name", "OpenGL::GL")
        deps.set_property("glm", "cmake_file_name", "GLM")
        deps.set_property("glm", "cmake_target_name", "GLM::GLM")
        deps.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure(variables={"CMAKE_EXPORT_COMPILE_COMMANDS": "ON"})
        cmake.build(cli_args=["--clean-first"])

        build_compile_commands = os.path.join(self.build_folder, "compile_commands.json")
        root_compile_commands = os.path.join(self.source_folder, "compile_commands.json")
        if os.path.exists(build_compile_commands):
            shutil.copy2(build_compile_commands, root_compile_commands)
            self.output.info("Copied compile_commands.json to project root")
