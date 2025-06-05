.PHONY: all conan cmake build

all: cmake build

conan:
	@conan install . --output-folder=build --build=missing --profile=conanprofile

cmake: conan
	@cmake -B build -S . -DCMAKE_TOOLCHAIN_FILE=conan_toolchain.cmake -G "Ninja"

build:
	@cmake --build build -j

clean:
	@git clean -f -d -X