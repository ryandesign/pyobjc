"""
Wrappers for the "ReplayKit" framework on macOS.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
"""
import os

from pyobjc_setup import setup, Extension

VERSION = "9.1"

setup(
    name="pyobjc-framework-ReplayKit",
    description="Wrappers for the framework ReplayKit on macOS",
    min_os_level="10.16",
    packages=["ReplayKit"],
    ext_modules=[
        Extension(
            "ReplayKit._ReplayKit",
            ["Modules/_ReplayKit.m"],
            extra_link_args=["-framework", "ReplayKit"],
            py_limited_api=True,
            depends=[
                os.path.join("Modules", fn)
                for fn in os.listdir("Modules")
                if fn.startswith("_ReplayKit")
            ],
        )
    ],
    version=VERSION,
    install_requires=["pyobjc-core>=" + VERSION, "pyobjc-framework-Cocoa>=" + VERSION],
    long_description=__doc__,
    options={"bdist_wheel": {"py_limited_api": "cp36"}},
)
