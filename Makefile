.PHONY: init conan_init conan_install conan_build conan_build_and_install exec tests

# Default build type
BUILD_TYPE ?= $(CHECK_BUILD_DIR_BY_TYPE)

BUILD_DIR = ./build/$(CHECK_BUILD_DIR_BY_TYPE)

CHECK_BUILD_DIR_BY_TYPE := $(if $(wildcard ./build/Debug),Debug,Release)

PATH := $(PATH):/github/home/.local/bin

init: 
	sudo apt update
	sudo apt install -y pipx
	pipx install conan

conan_init: 
	conan profile detect
	conan profile show
	$(MAKE) conan_install

conan_install:
	conan install . --build=missing -c tools.system.package_manager:mode=install -c tools.system.package_manager:sudo=True

conan_build:
	conan build .

conan_install_and_build: conan_install conan_build

exec:
	$(BUILD_DIR)/MyOpenGLProject

tests:
	$(BUILD_DIR)/tests $(ARGS)