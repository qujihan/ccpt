# This script executes after the project is generated from your cookiecutter.
# Details about hooks can be found in the cookiecutter documentation:
# https://cookiecutter.readthedocs.io/en/latest/advanced/hooks.html
#
# An example of a post-hook would be to remove parts of the project
# directory tree based on some configuration values.

import os
from cookiecutter.utils import rmtree

def conditional_remove(condition, path):
    if condition:
        if os.path.isfile(path):
            os.remove(path)
        else:
            rmtree(path)

conditional_remove("{{ cookiecutter.build_type }}" == "XMake", "cmake")
conditional_remove("{{ cookiecutter.build_type }}" == "XMake", "CMakeLists.txt")
conditional_remove("{{ cookiecutter.build_type }}" == "CMake", "xmake.lua")
print("The project {{ cookiecutter.project_slug }} was successfully generated!")