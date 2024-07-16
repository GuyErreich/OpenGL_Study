.PHONY: init conan_init conan_install conan_build conan_build_and_install

init: 
	sudo apt update
	sudo apt install pipx
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