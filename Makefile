.PHONY: init _install build build_and_install run tests

# Default build type
BUILD_TYPE ?= $(CHECK_BUILD_DIR_BY_TYPE)

BUILD_DIR = ./build/$(CHECK_BUILD_DIR_BY_TYPE)

CHECK_BUILD_DIR_BY_TYPE := $(if $(wildcard ./build/Debug),Debug,Release)

init: 
	sudo apt update
	sudo apt install -y pipx
	pipx install conan 
	conan profile detect
	conan profile show

install:
	conan install . --build=missing -c tools.system.package_manager:mode=install -c tools.system.package_manager:sudo=True

build:
	conan build . $(ARGS)

run:
	$(BUILD_DIR)/MyOpenGLProject

tests:
	$(BUILD_DIR)/tests $(ARGS)