set_xmakever("2.9.7")
set_project("{{ cookiecutter.project_slug }}")

set_allowedplats("windows", "linux", "macosx")
set_allowedmodes("debug", "release")

set_languages("c++{{ cookiecutter.cxx_minimum_standard }}")

add_requires("gtest", {configs = {main = false, gmock = true}})

target("objs")
    set_kind("object")
    add_files("src/*.cc")

target("main")
    set_kind("binary")
    add_deps("objs")
    add_files("main.cc")

target("unittests")
    set_kind("binary")
    add_packages("gtest")
    add_files("tests/*.cc")
    add_deps("objs")
    add_includedirs("src")
    add_tests("default")
    set_default(false)