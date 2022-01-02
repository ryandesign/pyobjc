# This file is generated by objective.metadata
#
# Last update: Thu Dec  2 21:36:33 2021
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
misc.update(
    {
        "GCMicroGamepadSnapshotData": objc.createStructType(
            "GameController.GCMicroGamepadSnapshotData",
            b"{_GCMicroGamepadSnapshotData=SSffff}",
            ["version", "size", "dpadX", "dpadY", "buttonA", "buttonX"],
            None,
            1,
        ),
        "GCQuaternion": objc.createStructType(
            "GameController.GCQuaternion", b"{GCQuaternion=dddd}", ["x", "y", "z", "w"]
        ),
        "GCExtendedGamepadValueChangedHandler": objc.createStructType(
            "GameController.GCExtendedGamepadValueChangedHandler",
            b"{_GCGamepadSnapShotDataV100=SSffffffff}",
            [
                "version",
                "size",
                "dpadX",
                "dpadY",
                "buttonA",
                "buttonB",
                "buttonX",
                "buttonY",
                "leftShoulder",
                "rightShoulder",
            ],
        ),
        "GCAcceleration": objc.createStructType(
            "GameController.GCAcceleration", b"{_GCAcceleration=ddd}", ["x", "y", "z"]
        ),
        "GCGamepadSnapShotDataV100": objc.createStructType(
            "GameController.GCGamepadSnapShotDataV100",
            b"{_GCGamepadSnapShotDataV100=SSffffffff}",
            [
                "version",
                "size",
                "dpadX",
                "dpadY",
                "buttonA",
                "buttonB",
                "buttonX",
                "buttonY",
                "leftShoulder",
                "rightShoulder",
            ],
            None,
            1,
        ),
        "GCEulerAngles": objc.createStructType(
            "GameController.GCEulerAngles",
            b"{_GCEulerAngles=ddd}",
            ["pitch", "yaw", "roll"],
        ),
        "GCExtendedGamepadSnapShotDataV100": objc.createStructType(
            "GameController.GCExtendedGamepadSnapShotDataV100",
            b"{_GCExtendedGamepadSnapShotDataV100=SSffffffffffffff}",
            [
                "version",
                "size",
                "dpadX",
                "dpadY",
                "buttonA",
                "buttonB",
                "buttonX",
                "buttonY",
                "leftShoulder",
                "rightShoulder",
                "leftThumbstickX",
                "leftThumbstickY",
                "rightThumbstickX",
                "rightThumbstickY",
                "leftTrigger",
                "rightTrigger",
            ],
            None,
            1,
        ),
        "GCRotationRate": objc.createStructType(
            "GameController.GCRotationRate", b"{_GCRotationRate=ddd}", ["x", "y", "z"]
        ),
        "GCMicroGamepadSnapShotDataV100": objc.createStructType(
            "GameController.GCMicroGamepadSnapShotDataV100",
            b"{_GCMicroGamepadSnapShotDataV100=SSffff}",
            ["version", "size", "dpadX", "dpadY", "buttonA", "buttonX"],
            None,
            1,
        ),
        "GCExtendedGamepadSnapshotData": objc.createStructType(
            "GameController.GCExtendedGamepadSnapshotData",
            b"{_GCExtendedGamepadSnapshotData=SSffffffffffffffZZZ}",
            [
                "version",
                "size",
                "dpadX",
                "dpadY",
                "buttonA",
                "buttonB",
                "buttonX",
                "buttonY",
                "leftShoulder",
                "rightShoulder",
                "leftThumbstickX",
                "leftThumbstickY",
                "rightThumbstickX",
                "rightThumbstickY",
                "leftTrigger",
                "rightTrigger",
                "supportsClickableThumbsticks",
                "leftThumbstickButton",
                "rightThumbstickButton",
            ],
            None,
            1,
        ),
    }
)
constants = """$GCControllerDidBecomeCurrentNotification$GCControllerDidConnectNotification$GCControllerDidDisconnectNotification$GCControllerDidStopBeingCurrentNotification$GCCurrentExtendedGamepadSnapshotDataVersion@q$GCCurrentMicroGamepadSnapshotDataVersion@q$GCHapticDurationInfinite@f$GCHapticsLocalityAll$GCHapticsLocalityDefault$GCHapticsLocalityHandles$GCHapticsLocalityLeftHandle$GCHapticsLocalityLeftTrigger$GCHapticsLocalityRightHandle$GCHapticsLocalityRightTrigger$GCHapticsLocalityTriggers$GCInputButtonA$GCInputButtonB$GCInputButtonHome$GCInputButtonMenu$GCInputButtonOptions$GCInputButtonShare$GCInputButtonX$GCInputButtonY$GCInputDirectionPad$GCInputDirectionalCardinalDpad$GCInputDirectionalCenterButton$GCInputDirectionalDpad$GCInputDirectionalTouchSurfaceButton$GCInputDualShockTouchpadButton$GCInputDualShockTouchpadOne$GCInputDualShockTouchpadTwo$GCInputLeftShoulder$GCInputLeftThumbstick$GCInputLeftThumbstickButton$GCInputLeftTrigger$GCInputMicroGamepadButtonA$GCInputMicroGamepadButtonMenu$GCInputMicroGamepadButtonX$GCInputMicroGamepadDpad$GCInputRightShoulder$GCInputRightThumbstick$GCInputRightThumbstickButton$GCInputRightTrigger$GCInputXboxPaddleFour$GCInputXboxPaddleOne$GCInputXboxPaddleThree$GCInputXboxPaddleTwo$GCKeyA$GCKeyApplication$GCKeyB$GCKeyBackslash$GCKeyC$GCKeyCapsLock$GCKeyCloseBracket$GCKeyCodeApplication@q$GCKeyCodeBackslash@q$GCKeyCodeCapsLock@q$GCKeyCodeCloseBracket@q$GCKeyCodeComma@q$GCKeyCodeDeleteForward@q$GCKeyCodeDeleteOrBackspace@q$GCKeyCodeDownArrow@q$GCKeyCodeEight@q$GCKeyCodeEnd@q$GCKeyCodeEqualSign@q$GCKeyCodeEscape@q$GCKeyCodeF1@q$GCKeyCodeF10@q$GCKeyCodeF11@q$GCKeyCodeF12@q$GCKeyCodeF13@q$GCKeyCodeF14@q$GCKeyCodeF15@q$GCKeyCodeF16@q$GCKeyCodeF17@q$GCKeyCodeF18@q$GCKeyCodeF19@q$GCKeyCodeF2@q$GCKeyCodeF20@q$GCKeyCodeF3@q$GCKeyCodeF4@q$GCKeyCodeF5@q$GCKeyCodeF6@q$GCKeyCodeF7@q$GCKeyCodeF8@q$GCKeyCodeF9@q$GCKeyCodeFive@q$GCKeyCodeFour@q$GCKeyCodeGraveAccentAndTilde@q$GCKeyCodeHome@q$GCKeyCodeHyphen@q$GCKeyCodeInsert@q$GCKeyCodeInternational1@q$GCKeyCodeInternational2@q$GCKeyCodeInternational3@q$GCKeyCodeInternational4@q$GCKeyCodeInternational5@q$GCKeyCodeInternational6@q$GCKeyCodeInternational7@q$GCKeyCodeInternational8@q$GCKeyCodeInternational9@q$GCKeyCodeKeyA@q$GCKeyCodeKeyB@q$GCKeyCodeKeyC@q$GCKeyCodeKeyD@q$GCKeyCodeKeyE@q$GCKeyCodeKeyF@q$GCKeyCodeKeyG@q$GCKeyCodeKeyH@q$GCKeyCodeKeyI@q$GCKeyCodeKeyJ@q$GCKeyCodeKeyK@q$GCKeyCodeKeyL@q$GCKeyCodeKeyM@q$GCKeyCodeKeyN@q$GCKeyCodeKeyO@q$GCKeyCodeKeyP@q$GCKeyCodeKeyQ@q$GCKeyCodeKeyR@q$GCKeyCodeKeyS@q$GCKeyCodeKeyT@q$GCKeyCodeKeyU@q$GCKeyCodeKeyV@q$GCKeyCodeKeyW@q$GCKeyCodeKeyX@q$GCKeyCodeKeyY@q$GCKeyCodeKeyZ@q$GCKeyCodeKeypad0@q$GCKeyCodeKeypad1@q$GCKeyCodeKeypad2@q$GCKeyCodeKeypad3@q$GCKeyCodeKeypad4@q$GCKeyCodeKeypad5@q$GCKeyCodeKeypad6@q$GCKeyCodeKeypad7@q$GCKeyCodeKeypad8@q$GCKeyCodeKeypad9@q$GCKeyCodeKeypadAsterisk@q$GCKeyCodeKeypadEnter@q$GCKeyCodeKeypadEqualSign@q$GCKeyCodeKeypadHyphen@q$GCKeyCodeKeypadNumLock@q$GCKeyCodeKeypadPeriod@q$GCKeyCodeKeypadPlus@q$GCKeyCodeKeypadSlash@q$GCKeyCodeLANG1@q$GCKeyCodeLANG2@q$GCKeyCodeLANG3@q$GCKeyCodeLANG4@q$GCKeyCodeLANG5@q$GCKeyCodeLANG6@q$GCKeyCodeLANG7@q$GCKeyCodeLANG8@q$GCKeyCodeLANG9@q$GCKeyCodeLeftAlt@q$GCKeyCodeLeftArrow@q$GCKeyCodeLeftControl@q$GCKeyCodeLeftGUI@q$GCKeyCodeLeftShift@q$GCKeyCodeNine@q$GCKeyCodeNonUSBackslash@q$GCKeyCodeNonUSPound@q$GCKeyCodeOne@q$GCKeyCodeOpenBracket@q$GCKeyCodePageDown@q$GCKeyCodePageUp@q$GCKeyCodePause@q$GCKeyCodePeriod@q$GCKeyCodePower@q$GCKeyCodePrintScreen@q$GCKeyCodeQuote@q$GCKeyCodeReturnOrEnter@q$GCKeyCodeRightAlt@q$GCKeyCodeRightArrow@q$GCKeyCodeRightControl@q$GCKeyCodeRightGUI@q$GCKeyCodeRightShift@q$GCKeyCodeScrollLock@q$GCKeyCodeSemicolon@q$GCKeyCodeSeven@q$GCKeyCodeSix@q$GCKeyCodeSlash@q$GCKeyCodeSpacebar@q$GCKeyCodeTab@q$GCKeyCodeThree@q$GCKeyCodeTwo@q$GCKeyCodeUpArrow@q$GCKeyCodeZero@q$GCKeyComma$GCKeyD$GCKeyDeleteForward$GCKeyDeleteOrBackspace$GCKeyDownArrow$GCKeyE$GCKeyEight$GCKeyEnd$GCKeyEqualSign$GCKeyEscape$GCKeyF$GCKeyF1$GCKeyF10$GCKeyF11$GCKeyF12$GCKeyF13$GCKeyF14$GCKeyF15$GCKeyF16$GCKeyF17$GCKeyF18$GCKeyF19$GCKeyF2$GCKeyF20$GCKeyF3$GCKeyF4$GCKeyF5$GCKeyF6$GCKeyF7$GCKeyF8$GCKeyF9$GCKeyFive$GCKeyFour$GCKeyG$GCKeyGraveAccentAndTilde$GCKeyH$GCKeyHome$GCKeyHyphen$GCKeyI$GCKeyInsert$GCKeyInternational1$GCKeyInternational2$GCKeyInternational3$GCKeyInternational4$GCKeyInternational5$GCKeyInternational6$GCKeyInternational7$GCKeyInternational8$GCKeyInternational9$GCKeyJ$GCKeyK$GCKeyKeypad0$GCKeyKeypad1$GCKeyKeypad2$GCKeyKeypad3$GCKeyKeypad4$GCKeyKeypad5$GCKeyKeypad6$GCKeyKeypad7$GCKeyKeypad8$GCKeyKeypad9$GCKeyKeypadAsterisk$GCKeyKeypadEnter$GCKeyKeypadEqualSign$GCKeyKeypadHyphen$GCKeyKeypadNumLock$GCKeyKeypadPeriod$GCKeyKeypadPlus$GCKeyKeypadSlash$GCKeyL$GCKeyLANG1$GCKeyLANG2$GCKeyLANG3$GCKeyLANG4$GCKeyLANG5$GCKeyLANG6$GCKeyLANG7$GCKeyLANG8$GCKeyLANG9$GCKeyLeftAlt$GCKeyLeftArrow$GCKeyLeftControl$GCKeyLeftGUI$GCKeyLeftShift$GCKeyM$GCKeyN$GCKeyNine$GCKeyNonUSBackslash$GCKeyNonUSPound$GCKeyO$GCKeyOne$GCKeyOpenBracket$GCKeyP$GCKeyPageDown$GCKeyPageUp$GCKeyPause$GCKeyPeriod$GCKeyPower$GCKeyPrintScreen$GCKeyQ$GCKeyQuote$GCKeyR$GCKeyReturnOrEnter$GCKeyRightAlt$GCKeyRightArrow$GCKeyRightControl$GCKeyRightGUI$GCKeyRightShift$GCKeyS$GCKeyScrollLock$GCKeySemicolon$GCKeySeven$GCKeySix$GCKeySlash$GCKeySpacebar$GCKeyT$GCKeyTab$GCKeyThree$GCKeyTwo$GCKeyU$GCKeyUpArrow$GCKeyV$GCKeyW$GCKeyX$GCKeyY$GCKeyZ$GCKeyZero$GCKeyboardDidConnectNotification$GCKeyboardDidDisconnectNotification$GCMouseDidBecomeCurrentNotification$GCMouseDidConnectNotification$GCMouseDidDisconnectNotification$GCMouseDidStopBeingCurrentNotification$GCProductCategoryCoalescedRemote$GCProductCategoryControlCenterRemote$GCProductCategoryDualSense$GCProductCategoryDualShock4$GCProductCategoryKeyboard$GCProductCategoryMFi$GCProductCategoryMouse$GCProductCategorySiriRemote1stGen$GCProductCategorySiriRemote2ndGen$GCProductCategoryUniversalElectronicsRemote$GCProductCategoryXboxOne$"""
enums = """$GCControllerPlayerIndex1@0$GCControllerPlayerIndex2@1$GCControllerPlayerIndex3@2$GCControllerPlayerIndex4@3$GCControllerPlayerIndexUnset@-1$GCDeviceBatteryStateCharging@1$GCDeviceBatteryStateDischarging@0$GCDeviceBatteryStateFull@2$GCDeviceBatteryStateUnknown@-1$GCDualSenseAdaptiveTriggerModeFeedback@1$GCDualSenseAdaptiveTriggerModeOff@0$GCDualSenseAdaptiveTriggerModeVibration@3$GCDualSenseAdaptiveTriggerModeWeapon@2$GCDualSenseAdaptiveTriggerStatusFeedbackLoadApplied@1$GCDualSenseAdaptiveTriggerStatusFeedbackNoLoad@0$GCDualSenseAdaptiveTriggerStatusUnknown@-1$GCDualSenseAdaptiveTriggerStatusVibrationIsVibrating@6$GCDualSenseAdaptiveTriggerStatusVibrationNotVibrating@5$GCDualSenseAdaptiveTriggerStatusWeaponFired@4$GCDualSenseAdaptiveTriggerStatusWeaponFiring@3$GCDualSenseAdaptiveTriggerStatusWeaponReady@2$GCExtendedGamepadSnapshotDataVersion1@256$GCExtendedGamepadSnapshotDataVersion2@257$GCMicroGamepadSnapshotDataVersion1@256$GCSystemGestureStateAlwaysReceive@1$GCSystemGestureStateDisabled@2$GCSystemGestureStateEnabled@0$GCTouchStateDown@1$GCTouchStateMoving@2$GCTouchStateUp@0$"""
misc.update({})
functions = {
    "GCExtendedGamepadSnapshotDataFromNSData": (
        b"Z^{_GCExtendedGamepadSnapshotData=SSffffffffffffffZZZ}@",
        "",
        {"arguments": {0: {"type_modifier": "o"}}},
    ),
    "NSDataFromGCMicroGamepadSnapShotDataV100": (
        b"@^{_GCMicroGamepadSnapShotDataV100=SSffff}",
        "",
        {"arguments": {0: {"type_modifier": "n"}}},
    ),
    "GCGamepadSnapShotDataV100FromNSData": (
        b"Z^{_GCGamepadSnapShotDataV100=SSffffffff}@",
        "",
        {"arguments": {0: {"type_modifier": "o"}}},
    ),
    "NSDataFromGCMicroGamepadSnapshotData": (
        b"@^{_GCMicroGamepadSnapshotData=SSffff}",
        "",
        {"arguments": {0: {"type_modifier": "n"}}},
    ),
    "NSDataFromGCGamepadSnapShotDataV100": (
        b"@^{_GCGamepadSnapShotDataV100=SSffffffff}",
        "",
        {"arguments": {0: {"type_modifier": "n"}}},
    ),
    "GCMicroGamepadSnapshotDataFromNSData": (
        b"Z^{_GCMicroGamepadSnapshotData=SSffff}@",
        "",
        {"arguments": {0: {"type_modifier": "o"}}},
    ),
    "GCExtendedGamepadSnapShotDataV100FromNSData": (
        b"Z^{_GCExtendedGamepadSnapShotDataV100=SSffffffffffffff}@",
        "",
        {"arguments": {0: {"type_modifier": "o"}}},
    ),
    "GCMicroGamepadSnapShotDataV100FromNSData": (
        b"Z^{_GCMicroGamepadSnapShotDataV100=SSffff}@",
        "",
        {"arguments": {0: {"type_modifier": "o"}}},
    ),
    "NSDataFromGCExtendedGamepadSnapShotDataV100": (
        b"@^{_GCExtendedGamepadSnapShotDataV100=SSffffffffffffff}",
    ),
    "NSDataFromGCExtendedGamepadSnapshotData": (
        b"@^{_GCExtendedGamepadSnapshotData=SSffffffffffffffZZZ}",
        "",
        {"arguments": {0: {"type_modifier": "n"}}},
    ),
}
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(
        b"GCController",
        b"controllerPausedHandler",
        {
            "retval": {
                "callable": {
                    "retval": {"type": b"v"},
                    "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                }
            }
        },
    )
    r(b"GCController", b"isAttachedToDevice", {"retval": {"type": b"Z"}})
    r(b"GCController", b"isSnapshot", {"retval": {"type": b"Z"}})
    r(
        b"GCController",
        b"setControllerPausedHandler:",
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
    r(
        b"GCController",
        b"setShouldMonitorBackgroundEvents",
        {"arguments": {2: {"type": "Z"}}},
    )
    r(
        b"GCController",
        b"setShouldMonitorBackgroundEvents:",
        {"arguments": {2: {"type": b"Z"}}},
    )
    r(b"GCController", b"shouldMonitorBackgroundEvents", {"retval": {"type": b"Z"}})
    r(
        b"GCController",
        b"startWirelessControllerDiscoveryWithCompletionHandler:",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}},
                    }
                }
            }
        },
    )
    r(b"GCController", b"supportsHIDDevice:", {"retval": {"type": b"Z"}})
    r(
        b"GCControllerAxisInput",
        b"setValueChangedHandler:",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"f"},
                        },
                    }
                }
            }
        },
    )
    r(
        b"GCControllerAxisInput",
        b"valueChangedHandler",
        {
            "retval": {
                "callable": {
                    "retval": {"type": b"v"},
                    "arguments": {
                        0: {"type": b"^v"},
                        1: {"type": b"@"},
                        2: {"type": b"f"},
                    },
                }
            }
        },
    )
    r(b"GCControllerButtonInput", b"isPressed", {"retval": {"type": b"Z"}})
    r(b"GCControllerButtonInput", b"isTouched", {"retval": {"type": b"Z"}})
    r(
        b"GCControllerButtonInput",
        b"pressedChangedHandler",
        {
            "retval": {
                "callable": {
                    "retval": {"type": b"v"},
                    "arguments": {
                        0: {"type": b"^v"},
                        1: {"type": b"@"},
                        2: {"type": b"f"},
                        3: {"type": b"Z"},
                    },
                }
            }
        },
    )
    r(
        b"GCControllerButtonInput",
        b"setPressedChangedHandler:",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"f"},
                            3: {"type": b"Z"},
                        },
                    }
                }
            }
        },
    )
    r(
        b"GCControllerButtonInput",
        b"setTouchedChangedHandler:",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"f"},
                            3: {"type": b"Z"},
                            4: {"type": b"Z"},
                        },
                    }
                }
            }
        },
    )
    r(
        b"GCControllerButtonInput",
        b"setValueChangedHandler:",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"f"},
                            3: {"type": b"Z"},
                        },
                    }
                }
            }
        },
    )
    r(
        b"GCControllerButtonInput",
        b"touchedChangedHandler",
        {
            "retval": {
                "callable": {
                    "retval": {"type": b"v"},
                    "arguments": {
                        0: {"type": b"^v"},
                        1: {"type": b"@"},
                        2: {"type": b"f"},
                        3: {"type": b"Z"},
                        4: {"type": b"Z"},
                    },
                }
            }
        },
    )
    r(
        b"GCControllerButtonInput",
        b"valueChangedHandler",
        {
            "retval": {
                "callable": {
                    "retval": {"type": b"v"},
                    "arguments": {
                        0: {"type": b"^v"},
                        1: {"type": b"@"},
                        2: {"type": b"f"},
                        3: {"type": b"Z"},
                    },
                }
            }
        },
    )
    r(
        b"GCControllerDirectionPad",
        b"setValueChangedHandler:",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"f"},
                            3: {"type": b"f"},
                        },
                    }
                }
            }
        },
    )
    r(
        b"GCControllerDirectionPad",
        b"valueChangedHandler",
        {
            "retval": {
                "callable": {
                    "retval": {"type": b"v"},
                    "arguments": {
                        0: {"type": b"^v"},
                        1: {"type": b"@"},
                        2: {"type": b"f"},
                        3: {"type": b"f"},
                    },
                }
            }
        },
    )
    r(b"GCControllerElement", b"isAnalog", {"retval": {"type": b"Z"}})
    r(b"GCControllerElement", b"isBoundToSystemGesture", {"retval": {"type": b"Z"}})
    r(
        b"GCControllerTouchpad",
        b"reportsAbsoluteTouchSurfaceValues",
        {"retval": {"type": b"Z"}},
    )
    r(
        b"GCControllerTouchpad",
        b"setReportsAbsoluteTouchSurfaceValues:",
        {"arguments": {2: {"type": b"Z"}}},
    )
    r(
        b"GCControllerTouchpad",
        b"setTouchDown:",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"f"},
                            2: {"type": b"f"},
                            3: {"type": b"f"},
                            4: {"type": b"Z"},
                        },
                    }
                }
            }
        },
    )
    r(
        b"GCControllerTouchpad",
        b"setTouchMoved:",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"f"},
                            2: {"type": b"f"},
                            3: {"type": b"f"},
                            4: {"type": b"Z"},
                        },
                    }
                }
            }
        },
    )
    r(
        b"GCControllerTouchpad",
        b"setTouchUp:",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"f"},
                            2: {"type": b"f"},
                            3: {"type": b"f"},
                            4: {"type": b"Z"},
                        },
                    }
                }
            }
        },
    )
    r(
        b"GCControllerTouchpad",
        b"setValueForXAxis:yAxis:touchDown:buttonValue:",
        {"arguments": {4: {"type": b"Z"}}},
    )
    r(
        b"GCControllerTouchpad",
        b"touchDown",
        {
            "retval": {
                "callable": {
                    "retval": {"type": b"v"},
                    "arguments": {
                        0: {"type": b"^v"},
                        1: {"type": b"f"},
                        2: {"type": b"f"},
                        3: {"type": b"f"},
                        4: {"type": b"Z"},
                    },
                }
            }
        },
    )
    r(
        b"GCControllerTouchpad",
        b"touchMoved",
        {
            "retval": {
                "callable": {
                    "retval": {"type": b"v"},
                    "arguments": {
                        0: {"type": b"^v"},
                        1: {"type": b"f"},
                        2: {"type": b"f"},
                        3: {"type": b"f"},
                        4: {"type": b"Z"},
                    },
                }
            }
        },
    )
    r(
        b"GCControllerTouchpad",
        b"touchUp",
        {
            "retval": {
                "callable": {
                    "retval": {"type": b"v"},
                    "arguments": {
                        0: {"type": b"^v"},
                        1: {"type": b"f"},
                        2: {"type": b"f"},
                        3: {"type": b"f"},
                        4: {"type": b"Z"},
                    },
                }
            }
        },
    )
    r(
        b"GCEventViewController",
        b"controllerUserInteractionEnabled",
        {"retval": {"type": "Z"}},
    )
    r(
        b"GCEventViewController",
        b"setControllerUserInteractionEnabled:",
        {"arguments": {2: {"type": "Z"}}},
    )
    r(
        b"GCExtendedGamepad",
        b"setValueChangedHandler:",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"@"},
                        },
                    }
                }
            }
        },
    )
    r(
        b"GCExtendedGamepad",
        b"valueChangedHandler",
        {
            "retval": {
                "callable": {
                    "retval": {"type": b"v"},
                    "arguments": {
                        0: {"type": b"^v"},
                        1: {"type": b"@"},
                        2: {"type": b"@"},
                    },
                }
            }
        },
    )
    r(
        b"GCGamepad",
        b"setValueChangedHandler:",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"@"},
                        },
                    }
                }
            }
        },
    )
    r(
        b"GCGamepad",
        b"valueChangedHandler",
        {
            "retval": {
                "callable": {
                    "retval": {"type": b"v"},
                    "arguments": {
                        0: {"type": b"^v"},
                        1: {"type": b"@"},
                        2: {"type": b"@"},
                    },
                }
            }
        },
    )
    r(b"GCKeyboardInput", b"isAnyKeyPressed", {"retval": {"type": b"Z"}})
    r(
        b"GCKeyboardInput",
        b"keyChangedHandler",
        {
            "retval": {
                "callable": {
                    "retval": {"type": b"v"},
                    "arguments": {
                        0: {"type": b"^v"},
                        1: {"type": b"@"},
                        2: {"type": b"@"},
                        3: {"type": b"q"},
                        4: {"type": b"Z"},
                    },
                }
            }
        },
    )
    r(
        b"GCKeyboardInput",
        b"setKeyChangedHandler:",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"@"},
                            3: {"type": b"q"},
                            4: {"type": b"Z"},
                        },
                    }
                }
            }
        },
    )
    r(b"GCMicroGamepad", b"allowsRotation", {"retval": {"type": "Z"}})
    r(b"GCMicroGamepad", b"reportsAbsoluteDpadValues", {"retval": {"type": "Z"}})
    r(b"GCMicroGamepad", b"setAllowsRotation:", {"arguments": {2: {"type": "Z"}}})
    r(
        b"GCMicroGamepad",
        b"setReportsAbsoluteDpadValues:",
        {"arguments": {2: {"type": "Z"}}},
    )
    r(
        b"GCMicroGamepad",
        b"setValueChangedHandler:",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"@"},
                        },
                    }
                }
            }
        },
    )
    r(
        b"GCMicroGamepad",
        b"valueChangedHandler",
        {
            "retval": {
                "callable": {
                    "retval": {"type": b"v"},
                    "arguments": {
                        0: {"type": b"^v"},
                        1: {"type": b"@"},
                        2: {"type": b"@"},
                    },
                }
            }
        },
    )
    r(b"GCMotion", b"acceleration", {"retval": {"type": b"{_GCAcceleration=ddd}"}})
    r(b"GCMotion", b"gravity", {"retval": {"type": b"{_GCAcceleration=ddd}"}})
    r(b"GCMotion", b"hasAttitude", {"retval": {"type": b"Z"}})
    r(b"GCMotion", b"hasAttitudeAndRotationRate", {"retval": {"type": "Z"}})
    r(b"GCMotion", b"hasGravityAndUserAcceleration", {"retval": {"type": "Z"}})
    r(b"GCMotion", b"hasRotationRate", {"retval": {"type": b"Z"}})
    r(b"GCMotion", b"rotationRate", {"retval": {"type": b"{_GCRotationRate=ddd}"}})
    r(b"GCMotion", b"sensorsActive", {"retval": {"type": b"Z"}})
    r(b"GCMotion", b"sensorsRequireManualActivation", {"retval": {"type": b"Z"}})
    r(
        b"GCMotion",
        b"setAcceleration:",
        {"arguments": {2: {"type": b"{_GCAcceleration=ddd}"}}},
    )
    r(
        b"GCMotion",
        b"setGravity:",
        {"arguments": {2: {"type": b"{_GCAcceleration=ddd}"}}},
    )
    r(
        b"GCMotion",
        b"setRotationRate:",
        {"arguments": {2: {"type": b"{_GCRotationRate=ddd}"}}},
    )
    r(b"GCMotion", b"setSensorsActive:", {"arguments": {2: {"type": b"Z"}}})
    r(
        b"GCMotion",
        b"setUserAcceleration:",
        {"arguments": {2: {"type": b"{_GCAcceleration=ddd}"}}},
    )
    r(
        b"GCMotion",
        b"setValueChangedHandler:",
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
    r(b"GCMotion", b"userAcceleration", {"retval": {"type": b"{_GCAcceleration=ddd}"}})
    r(
        b"GCMotion",
        b"valueChangedHandler",
        {
            "retval": {
                "callable": {
                    "retval": {"type": b"v"},
                    "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                }
            }
        },
    )
    r(
        b"GCMouseInput",
        b"mouseMovedHandler",
        {
            "retval": {
                "callable": {
                    "retval": {"type": b"v"},
                    "arguments": {
                        0: {"type": b"^v"},
                        1: {"type": b"@"},
                        2: {"type": b"f"},
                        3: {"type": b"f"},
                    },
                }
            }
        },
    )
    r(
        b"GCMouseInput",
        b"setMouseMovedHandler:",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"f"},
                            3: {"type": b"f"},
                        },
                    }
                }
            }
        },
    )
    r(b"GCPhysicalInputProfile", b"hasRemappedElements", {"retval": {"type": "Z"}})
    r(b"NSObject", b"handlerQueue", {"required": True, "retval": {"type": b"@"}})
    r(
        b"NSObject",
        b"physicalInputProfile",
        {"required": True, "retval": {"type": b"@"}},
    )
    r(b"NSObject", b"productCategory", {"required": True, "retval": {"type": b"@"}})
    r(
        b"NSObject",
        b"setHandlerQueue:",
        {"required": True, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(b"NSObject", b"vendorName", {"required": True, "retval": {"type": b"@"}})
finally:
    objc._updatingMetadata(False)
expressions = {}

# END OF FILE
