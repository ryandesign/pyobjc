"""
Wrappers for the "SharedWithYouCore" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
"""

import os

from pyobjc_setup import Extension, setup

VERSION = "9.1"

setup(
    name="pyobjc-framework-SharedWithYouCore",
    description="Wrappers for the framework SharedWithYouCore on macOS",
    min_os_level="13.0",
    packages=["SharedWithYouCore"],
    ext_modules=[
        Extension(
            "SharedWithYouCore._SharedWithYouCore",
            ["Modules/_SharedWithYouCore.m"],
            extra_link_args=["-framework", "SharedWithYouCore"],
            py_limited_api=True,
            depends=[
                os.path.join("Modules", fn)
                for fn in os.listdir("Modules")
                if fn.startswith("_SharedWithYouCore")
            ],
        ),
    ],
    version=VERSION,
    install_requires=[
        "pyobjc-core>=" + VERSION,
        "pyobjc-framework-Cocoa>=" + VERSION,
    ],
    long_description=__doc__,
    options={"bdist_wheel": {"py_limited_api": "cp36"}},
)
