# This script executes before the project is generated from your cookiecutter.
# Details about hooks can be found in the cookiecutter documentation:
# https://cookiecutter.readthedocs.io/en/latest/advanced/hooks.html
#
# An example of a pre-hook would be to validate the provided input for a
# user configuration value and exit with an error upon failure.

import cookiecutter
import sys

def hook(context):
    build_type = context['cookiecutter']['build_type']
    print(f"build_type: {build_type}")  # 输出 build_type 以调试
    if 'XMake' in build_type:
        print("Removing 'generator'")  # 输出提示消息
        del context['cookiecutter']['generator']