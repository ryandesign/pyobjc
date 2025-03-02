"""
Wrappers for the "MetalFX" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
"""

import os

from pyobjc_setup import Extension, setup

VERSION = "9.1"

setup(
    name="pyobjc-framework-MetalFX",
    description="Wrappers for the framework MetalFX on macOS",
    min_os_level="13.0",
    packages=["MetalFX"],
    ext_modules=[
        Extension(
            "MetalFX._MetalFX",
            ["Modules/_MetalFX.m"],
            extra_link_args=["-framework", "MetalFX"],
            py_limited_api=True,
            depends=[
                os.path.join("Modules", fn)
                for fn in os.listdir("Modules")
                if fn.startswith("_MetalFX")
            ],
        ),
    ],
    version=VERSION,
    install_requires=[
        "pyobjc-core>=" + VERSION,
        "pyobjc-framework-Metal>=" + VERSION,
    ],
    long_description=__doc__,
    options={"bdist_wheel": {"py_limited_api": "cp36"}},
)
