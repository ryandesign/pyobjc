# This file is generated by objective.metadata
#
# Last update: Sun Jul 11 21:33:17 2021
#
# flake8: noqa

import objc, sys

if sys.maxsize > 2 ** 32:

    def sel32or64(a, b):
        return b

else:

    def sel32or64(a, b):
        return a


if objc.arch == "arm64":

    def selAorI(a, b):
        return a

else:

    def selAorI(a, b):
        return b


misc = {}
constants = """$$"""
enums = """$AUViewParametersDisplayFlag@4$AUViewPropertiesDisplayFlag@2$AUViewTitleDisplayFlag@1$"""
misc.update({})
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(
        b"AUAudioUnit",
        b"requestViewControllerWithCompletionHandler:",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                    }
                }
            }
        },
    )
    r(b"AUAudioUnitViewConfiguration", b"hostHasController", {"retval": {"type": b"Z"}})
    r(
        b"AUAudioUnitViewConfiguration",
        b"initWithWidth:height:hostHasController:",
        {"arguments": {4: {"type": b"Z"}}},
    )
    r(
        b"AUGenericView",
        b"setShowsExpertParameters:",
        {"arguments": {2: {"type": b"Z"}}},
    )
    r(b"AUGenericView", b"showsExpertParameters", {"retval": {"type": b"Z"}})
    r(
        b"CANetworkBrowserWindowController",
        b"isAVBSupported",
        {"retval": {"type": b"Z"}},
    )
    r(
        b"NSObject",
        b"customViewPersistentData",
        {"required": True, "retval": {"type": b"@"}},
    )
    r(
        b"NSObject",
        b"setCustomViewPersistentData:",
        {"required": True, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"null",
        b"requestViewControllerWithCompletionHandler:",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                    }
                }
            }
        },
    )
finally:
    objc._updatingMetadata(False)
expressions = {}

# END OF FILE
