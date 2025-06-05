file_name := "{{ cookiecutter.project_slug }}.pdf"
typst := "typst"

.PHONY: all build watch clean

all: build

build:
	${typst} c main.typ ${file_name} --font-path ./fonts --root .

watch:
	${typst} w main.typ ${file_name} --font-path ./fonts --root .

clean:
	rm -rf output/* ./*.pdf; git clean -df -X