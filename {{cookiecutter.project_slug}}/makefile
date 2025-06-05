DEBUG_DIR   = build/debug
RELEASE_DIR = build/release
CLANGD_DIR  = build/clangd

GENERATOR = {{ cookiecutter.generator }}

.PHONY: all clangd cmake build run clean

all: debug

clangd:
	@cmake -B ${CLANGD_DIR} -S . -G "${GENERATOR}" -DCMAKE_BUILD_TYPE=Debug -DCMAKE_EXPORT_COMPILE_COMMANDS=ON

debug: clangd
	@cmake -B ${DEBUG_DIR} -S . -G "${GENERATOR}" -DCMAKE_BUILD_TYPE=Debug
	@cmake --build ${DEBUG_DIR}

release: clangd
	@cmake -B ${RELEASE_DIR} -S . -G "${GENERATOR}" -DCMAKE_BUILD_TYPE=Release
	@cmake --build ${RELEASE_DIR}

clean:
	@rm -rf build