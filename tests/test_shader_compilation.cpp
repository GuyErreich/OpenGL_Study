#include <catch2/catch_test_macros.hpp>
#include <opengl_fixture.hpp>
#include <shader.h>

using namespace std;

TEST_CASE_METHOD(OpenGLFixture, "Shaders are computed", "[shader]") {
    try {
        REQUIRE_NOTHROW([&]() {
            Shader ourShader("3.3.shader.vs", "3.3.shader.fs");
            ourShader.use();
        }());
    } catch (const std::exception &e) {
        FAIL("Exception was thrown: " << e.what());
    } catch (...) {
        FAIL("Unknown exception was thrown");
    }
}