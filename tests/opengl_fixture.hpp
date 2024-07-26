#include <glad/glad.h>
#include <GLFW/glfw3.h>
#include <iostream>

using namespace std;

class OpenGLFixture {
public:
    GLFWwindow* window;

public:
    OpenGLFixture() {
        if (!glfwInit()) {
            throw runtime_error("Failed to initialize GLFW");
        }

        glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3);
        glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3);
        glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);

#ifdef __APPLE__
        glfwWindowHint(GLFW_OPENGL_FORWARD_COMPAT, GL_TRUE);
#endif

        window = glfwCreateWindow(800, 600, "OpenGL Test", NULL, NULL);
        if (!window) {
            glfwTerminate();
            throw runtime_error("Failed to create GLFW window");
        }

        glfwMakeContextCurrent(window);

        if (!gladLoadGLLoader((GLADloadproc)glfwGetProcAddress))
        {
            throw runtime_error("Failed to initialize GLAD");
        }
    }

    ~OpenGLFixture() {
        glfwDestroyWindow(window);
        glfwTerminate();
    }
};
