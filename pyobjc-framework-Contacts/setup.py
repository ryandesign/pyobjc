"""
Wrappers for the "Contacts" framework on macOS 10.11.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
"""

import os

from pyobjc_setup import Extension, setup

VERSION = "9.1"

setup(
    name="pyobjc-framework-Contacts",
    description="Wrappers for the framework Contacts on macOS",
    min_os_level="10.11",
    packages=["Contacts"],
    ext_modules=[
        Extension(
            "Contacts._Contacts",
            ["Modules/_Contacts.m"],
            extra_link_args=["-framework", "Contacts"],
            py_limited_api=True,
            depends=[
                os.path.join("Modules", fn)
                for fn in os.listdir("Modules")
                if fn.startswith("_Contacts")
            ],
        )
    ],
    version=VERSION,
    install_requires=["pyobjc-core>=" + VERSION, "pyobjc-framework-Cocoa>=" + VERSION],
    long_description=__doc__,
    options={"bdist_wheel": {"py_limited_api": "cp36"}},
)
