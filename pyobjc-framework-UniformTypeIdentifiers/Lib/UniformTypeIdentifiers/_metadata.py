# This file is generated by objective.metadata
#
# Last update: Sun Jul 11 21:54:51 2021
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
constants = """$UTTagClassFilenameExtension$UTTagClassMIMEType$UTType3DContent$UTTypeAIFF$UTTypeARReferenceObject$UTTypeAVI$UTTypeAliasFile$UTTypeAppleArchive$UTTypeAppleProtectedMPEG4Audio$UTTypeAppleProtectedMPEG4Video$UTTypeAppleScript$UTTypeApplication$UTTypeApplicationBundle$UTTypeApplicationExtension$UTTypeArchive$UTTypeAssemblyLanguageSource$UTTypeAudio$UTTypeAudiovisualContent$UTTypeBMP$UTTypeBZ2$UTTypeBinaryPropertyList$UTTypeBookmark$UTTypeBundle$UTTypeCHeader$UTTypeCPlusPlusHeader$UTTypeCPlusPlusSource$UTTypeCSource$UTTypeCalendarEvent$UTTypeCommaSeparatedText$UTTypeCompositeContent$UTTypeContact$UTTypeContent$UTTypeData$UTTypeDatabase$UTTypeDelimitedText$UTTypeDirectory$UTTypeDiskImage$UTTypeEPUB$UTTypeEXE$UTTypeEmailMessage$UTTypeExecutable$UTTypeFileURL$UTTypeFlatRTFD$UTTypeFolder$UTTypeFont$UTTypeFramework$UTTypeGIF$UTTypeGZIP$UTTypeHEIC$UTTypeHEIF$UTTypeHTML$UTTypeICNS$UTTypeICO$UTTypeImage$UTTypeInternetLocation$UTTypeInternetShortcut$UTTypeItem$UTTypeJPEG$UTTypeJSON$UTTypeJavaScript$UTTypeLivePhoto$UTTypeLog$UTTypeM3UPlaylist$UTTypeMIDI$UTTypeMP3$UTTypeMPEG$UTTypeMPEG2TransportStream$UTTypeMPEG2Video$UTTypeMPEG4Audio$UTTypeMPEG4Movie$UTTypeMakefile$UTTypeMessage$UTTypeMountPoint$UTTypeMovie$UTTypeOSAScript$UTTypeOSAScriptBundle$UTTypeObjectiveCPlusPlusSource$UTTypeObjectiveCSource$UTTypePDF$UTTypePHPScript$UTTypePKCS12$UTTypePNG$UTTypePackage$UTTypePerlScript$UTTypePlainText$UTTypePlaylist$UTTypePluginBundle$UTTypePresentation$UTTypePropertyList$UTTypePythonScript$UTTypeQuickLookGenerator$UTTypeQuickTimeMovie$UTTypeRAWImage$UTTypeRTF$UTTypeRTFD$UTTypeRealityFile$UTTypeResolvable$UTTypeRubyScript$UTTypeSVG$UTTypeSceneKitScene$UTTypeScript$UTTypeShellScript$UTTypeSourceCode$UTTypeSpotlightImporter$UTTypeSpreadsheet$UTTypeSwiftSource$UTTypeSymbolicLink$UTTypeSystemPreferencesPane$UTTypeTIFF$UTTypeTabSeparatedText$UTTypeText$UTTypeToDoItem$UTTypeURL$UTTypeURLBookmarkData$UTTypeUSD$UTTypeUSDZ$UTTypeUTF16ExternalPlainText$UTTypeUTF16PlainText$UTTypeUTF8PlainText$UTTypeUTF8TabSeparatedText$UTTypeUnixExecutable$UTTypeVCard$UTTypeVideo$UTTypeVolume$UTTypeWAV$UTTypeWebArchive$UTTypeWebP$UTTypeX509Certificate$UTTypeXML$UTTypeXMLPropertyList$UTTypeXPCService$UTTypeYAML$UTTypeZIP$"""
enums = """$$"""
misc.update({})
aliases = {"UT_AVAILABLE_END": "API_AVAILABLE_END"}
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(b"UTType", b"conformsToType:", {"retval": {"type": b"Z"}})
    r(b"UTType", b"isDeclared", {"retval": {"type": b"Z"}})
    r(b"UTType", b"isDynamic", {"retval": {"type": b"Z"}})
    r(b"UTType", b"isPublicType", {"retval": {"type": b"Z"}})
    r(b"UTType", b"isSubtypeOfType:", {"retval": {"type": b"Z"}})
    r(b"UTType", b"isSupertypeOfType:", {"retval": {"type": b"Z"}})
    r(b"null", b"conformsToType:", {"retval": {"type": b"Z"}})
    r(b"null", b"isSubtypeOfType:", {"retval": {"type": b"Z"}})
    r(b"null", b"isSupertypeOfType:", {"retval": {"type": b"Z"}})
finally:
    objc._updatingMetadata(False)
expressions = {}

# END OF FILE
