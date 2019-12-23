# This file is generated by objective.metadata
#
# Last update: Fri Aug 16 23:15:47 2019

import objc, sys

if sys.maxsize > 2 ** 32:

    def sel32or64(a, b):
        return b


else:

    def sel32or64(a, b):
        return a


misc = {}
constants = """$PDFAnnotationHighlightingModeInvert$PDFAnnotationHighlightingModeNone$PDFAnnotationHighlightingModeOutline$PDFAnnotationHighlightingModePush$PDFAnnotationKeyAction$PDFAnnotationKeyAdditionalActions$PDFAnnotationKeyAppearanceDictionary$PDFAnnotationKeyAppearanceState$PDFAnnotationKeyBorder$PDFAnnotationKeyBorderStyle$PDFAnnotationKeyColor$PDFAnnotationKeyContents$PDFAnnotationKeyDate$PDFAnnotationKeyDefaultAppearance$PDFAnnotationKeyDestination$PDFAnnotationKeyFlags$PDFAnnotationKeyHighlightingMode$PDFAnnotationKeyIconName$PDFAnnotationKeyInklist$PDFAnnotationKeyInteriorColor$PDFAnnotationKeyLineEndingStyles$PDFAnnotationKeyLinePoints$PDFAnnotationKeyName$PDFAnnotationKeyOpen$PDFAnnotationKeyPage$PDFAnnotationKeyParent$PDFAnnotationKeyPopup$PDFAnnotationKeyQuadPoints$PDFAnnotationKeyQuadding$PDFAnnotationKeyRect$PDFAnnotationKeySubtype$PDFAnnotationKeyTextLabel$PDFAnnotationKeyWidgetAppearanceDictionary$PDFAnnotationKeyWidgetBackgroundColor$PDFAnnotationKeyWidgetBorderColor$PDFAnnotationKeyWidgetCaption$PDFAnnotationKeyWidgetDefaultValue$PDFAnnotationKeyWidgetDownCaption$PDFAnnotationKeyWidgetFieldFlags$PDFAnnotationKeyWidgetFieldType$PDFAnnotationKeyWidgetMaxLen$PDFAnnotationKeyWidgetOptions$PDFAnnotationKeyWidgetRolloverCaption$PDFAnnotationKeyWidgetRotation$PDFAnnotationKeyWidgetTextLabelUI$PDFAnnotationKeyWidgetValue$PDFAnnotationLineEndingStyleCircle$PDFAnnotationLineEndingStyleClosedArrow$PDFAnnotationLineEndingStyleDiamond$PDFAnnotationLineEndingStyleNone$PDFAnnotationLineEndingStyleOpenArrow$PDFAnnotationLineEndingStyleSquare$PDFAnnotationSubtypeCircle$PDFAnnotationSubtypeFreeText$PDFAnnotationSubtypeHighlight$PDFAnnotationSubtypeInk$PDFAnnotationSubtypeLine$PDFAnnotationSubtypeLink$PDFAnnotationSubtypePopup$PDFAnnotationSubtypeSquare$PDFAnnotationSubtypeStamp$PDFAnnotationSubtypeStrikeOut$PDFAnnotationSubtypeText$PDFAnnotationSubtypeUnderline$PDFAnnotationSubtypeWidget$PDFAnnotationTextIconTypeComment$PDFAnnotationTextIconTypeHelp$PDFAnnotationTextIconTypeInsert$PDFAnnotationTextIconTypeKey$PDFAnnotationTextIconTypeNewParagraph$PDFAnnotationTextIconTypeNote$PDFAnnotationTextIconTypeParagraph$PDFAnnotationWidgetSubtypeButton$PDFAnnotationWidgetSubtypeChoice$PDFAnnotationWidgetSubtypeSignature$PDFAnnotationWidgetSubtypeText$PDFAppearanceCharacteristicsKeyBackgroundColor$PDFAppearanceCharacteristicsKeyBorderColor$PDFAppearanceCharacteristicsKeyCaption$PDFAppearanceCharacteristicsKeyDownCaption$PDFAppearanceCharacteristicsKeyRolloverCaption$PDFAppearanceCharacteristicsKeyRotation$PDFBorderKeyDashPattern$PDFBorderKeyLineWidth$PDFBorderKeyStyle$PDFDocumentAuthorAttribute$PDFDocumentCreationDateAttribute$PDFDocumentCreatorAttribute$PDFDocumentDidBeginFindNotification$PDFDocumentDidBeginPageFindNotification$PDFDocumentDidBeginPageWriteNotification$PDFDocumentDidBeginWriteNotification$PDFDocumentDidEndFindNotification$PDFDocumentDidEndPageFindNotification$PDFDocumentDidEndPageWriteNotification$PDFDocumentDidEndWriteNotification$PDFDocumentDidFindMatchNotification$PDFDocumentDidUnlockNotification$PDFDocumentKeywordsAttribute$PDFDocumentModificationDateAttribute$PDFDocumentOwnerPasswordOption$PDFDocumentProducerAttribute$PDFDocumentSubjectAttribute$PDFDocumentTitleAttribute$PDFDocumentUserPasswordOption$PDFThumbnailViewDocumentEditedNotification$PDFViewAnnotationHitNotification$PDFViewAnnotationWillHitNotification$PDFViewChangedHistoryNotification$PDFViewCopyPermissionNotification$PDFViewDisplayBoxChangedNotification$PDFViewDisplayModeChangedNotification$PDFViewDocumentChangedNotification$PDFViewPageChangedNotification$PDFViewPrintPermissionNotification$PDFViewScaleChangedNotification$PDFViewSelectionChangedNotification$PDFViewVisiblePagesChangedNotification$kPDFAnnotationKey_Action$kPDFAnnotationKey_AdditionalActions$kPDFAnnotationKey_AppearanceDictionary$kPDFAnnotationKey_AppearanceState$kPDFAnnotationKey_AppleExtras$kPDFAnnotationKey_Border$kPDFAnnotationKey_BorderStyle$kPDFAnnotationKey_Color$kPDFAnnotationKey_Contents$kPDFAnnotationKey_Date$kPDFAnnotationKey_DefaultAppearance$kPDFAnnotationKey_Destination$kPDFAnnotationKey_Flags$kPDFAnnotationKey_HighlightingMode$kPDFAnnotationKey_IconName$kPDFAnnotationKey_Inklist$kPDFAnnotationKey_InteriorColor$kPDFAnnotationKey_LineEndingStyles$kPDFAnnotationKey_LinePoints$kPDFAnnotationKey_Name$kPDFAnnotationKey_Open$kPDFAnnotationKey_Page$kPDFAnnotationKey_Parent$kPDFAnnotationKey_Popup$kPDFAnnotationKey_QuadPoints$kPDFAnnotationKey_Quadding$kPDFAnnotationKey_Rect$kPDFAnnotationKey_Subtype$kPDFAnnotationKey_TextLabel$kPDFAnnotationKey_WidgetAppearanceDictionary$kPDFAnnotationKey_WidgetDefaultValue$kPDFAnnotationKey_WidgetFieldFlags$kPDFAnnotationKey_WidgetFieldType$kPDFAnnotationKey_WidgetMaxLen$kPDFAnnotationKey_WidgetOptions$kPDFAnnotationKey_WidgetTextLabelUI$kPDFAnnotationKey_WidgetValue$"""
constants = constants + "$kPDFDestinationUnspecifiedValue=" + sel32or64("f", "d") + "$"
enums = """$kPDFActionNamedFind@8$kPDFActionNamedFirstPage@3$kPDFActionNamedGoBack@5$kPDFActionNamedGoForward@6$kPDFActionNamedGoToPage@7$kPDFActionNamedLastPage@4$kPDFActionNamedNextPage@1$kPDFActionNamedNone@0$kPDFActionNamedPreviousPage@2$kPDFActionNamedPrint@9$kPDFActionNamedZoomIn@10$kPDFActionNamedZoomOut@11$kPDFAnnotationArea@4$kPDFBorderStyleBeveled@2$kPDFBorderStyleDashed@1$kPDFBorderStyleInset@3$kPDFBorderStyleSolid@0$kPDFBorderStyleUnderline@4$kPDFControlArea@16$kPDFDisplayBoxArtBox@4$kPDFDisplayBoxBleedBox@2$kPDFDisplayBoxCropBox@1$kPDFDisplayBoxMediaBox@0$kPDFDisplayBoxTrimBox@3$kPDFDisplayDirectionHorizontal@1$kPDFDisplayDirectionVertical@0$kPDFDisplaySinglePage@0$kPDFDisplaySinglePageContinuous@1$kPDFDisplayTwoUp@2$kPDFDisplayTwoUpContinuous@3$kPDFDocumentPermissionsNone@0$kPDFDocumentPermissionsOwner@2$kPDFDocumentPermissionsUser@1$kPDFIconArea@64$kPDFImageArea@256$kPDFInterpolationQualityHigh@2$kPDFInterpolationQualityLow@1$kPDFInterpolationQualityNone@0$kPDFLineStyleCircle@2$kPDFLineStyleClosedArrow@5$kPDFLineStyleDiamond@3$kPDFLineStyleNone@0$kPDFLineStyleOpenArrow@4$kPDFLineStyleSquare@1$kPDFLinkArea@8$kPDFMarkupTypeHighlight@0$kPDFMarkupTypeStrikeOut@1$kPDFMarkupTypeUnderline@2$kPDFNoArea@0$kPDFPageArea@1$kPDFPopupArea@128$kPDFPrintPageScaleDownToFit@2$kPDFPrintPageScaleNone@0$kPDFPrintPageScaleToFit@1$kPDFTextAnnotationIconComment@0$kPDFTextAnnotationIconHelp@3$kPDFTextAnnotationIconInsert@6$kPDFTextAnnotationIconKey@1$kPDFTextAnnotationIconNewParagraph@4$kPDFTextAnnotationIconNote@2$kPDFTextAnnotationIconParagraph@5$kPDFTextArea@2$kPDFTextFieldArea@32$kPDFWidgetCheckBoxControl@2$kPDFWidgetMixedState@-1$kPDFWidgetOffState@0$kPDFWidgetOnState@1$kPDFWidgetPushButtonControl@0$kPDFWidgetRadioButtonControl@1$kPDFWidgetUnknownControl@-1$"""
misc.update({})
aliases = {
    "PDFKitPlatformViewController": "NSViewController",
    "PDFKitPlatformEvent": "NSEvent",
    "PDFKitPlatformControl": "NSControl",
    "PDFPointZero": "NSZeroPoint",
    "PDFKitPlatformTextViewDelegate": "NSTextViewDelegate",
    "PDFRectZero": "NSZeroRect",
    "PDFKitPlatformButtonCell": "NSButtonCell",
    "PDFEdgeInsets": "NSEdgeInsets",
    "PDFKitPlatformButton": "NSButton",
    "PDFSize": "NSSize",
    "PDFRect": "NSRect",
    "kPDFImageArea": "FLT_MX",
    "PDFKitPlatformAccessibilityElement": "NSAccessibilityElement",
    "PDFKitPlatformTextView": "NSTextView",
    "PDFKitPlatformChoiceWidgetListView": "NSTableView",
    "PDFKitPlatformView": "NSView",
    "PDFSizeZero": "NSZeroSize",
    "kPDFDestinationUnspecifiedValue": "FLT_MAX",
    "PDFKitPlatformBezierPathElement": "NSBezierPathElement",
    "PDFKitPlatformColor": "NSColor",
    "PDFKitPlatformTextFieldCell": "NSTextFieldCell",
    "PDFKitPlatformScrollView": "NSScrollView",
    "PDFKitPlatformImageView": "NSImageView",
    "PDFKitPlatformTextFieldDidChangeText": "NSControlTextDidChangeNotification",
    "PDFPoint": "NSPoint",
    "PDFKitPlatformImage": "NSImage",
    "PDFKitPlatformChoiceWidgetComboBoxView": "NSPopUpButton",
    "PDFKitPlatformBezierPath": "NSBezierPath",
    "PDFKitPlatformTextFieldDidBeginEditing": "NSControlTextDidBeginEditingNotification",
    "PDFEdgeInsetsZero": "NSEdgeInsetsZero",
    "PDFKitPlatformTextFieldDidEndEditing": "NSControlTextDidEndEditingNotification",
    "PDFKitPlatformTextViewDidChangeSelection": "NSTextViewDidChangeSelectionNotification",
    "PDFKitPlatformTextField": "NSTextField",
    "PDFKitPlatformFont": "NSFont",
}
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(
        b"NSObject",
        b"PDFViewOpenPDF:forRemoteGoToAction:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"PDFViewPerformFind:",
        {"required": False, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"PDFViewPerformGoToPage:",
        {"required": False, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"PDFViewPerformPrint:",
        {"required": False, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"PDFViewPrintJobTitle:",
        {"required": False, "retval": {"type": b"@"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"PDFViewWillChangeScaleFactor:toScale:",
        {
            "required": False,
            "retval": {"type": sel32or64(b"f", b"d")},
            "arguments": {2: {"type": b"@"}, 3: {"type": sel32or64(b"f", b"d")}},
        },
    )
    r(
        b"NSObject",
        b"PDFViewWillClickOnLink:withURL:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"classForAnnotationClass:",
        {"required": False, "retval": {"type": "#"}, "arguments": {2: {"type": b"#"}}},
    )
    r(
        b"NSObject",
        b"classForAnnotationType:",
        {"required": False, "retval": {"type": "#"}, "arguments": {2: {"type": b"@"}}},
    )
    r(b"NSObject", b"classForPage", {"required": False, "retval": {"type": "#"}})
    r(
        b"NSObject",
        b"didMatchString:",
        {"required": False, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"documentDidBeginDocumentFind:",
        {"required": False, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"documentDidBeginPageFind:",
        {"required": False, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"documentDidEndDocumentFind:",
        {"required": False, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"documentDidEndPageFind:",
        {"required": False, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"documentDidFindMatch:",
        {"required": False, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"documentDidUnlock:",
        {"required": False, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(b"PDFActionResetForm", b"fieldsIncludedAreCleared", {"retval": {"type": b"Z"}})
    r(
        b"PDFActionResetForm",
        b"setFieldsIncludedAreCleared:",
        {"arguments": {2: {"type": b"Z"}}},
    )
    r(b"PDFAnnotation", b"allowsToggleToOff", {"retval": {"type": "Z"}})
    r(b"PDFAnnotation", b"hasAppearanceStream", {"retval": {"type": b"Z"}})
    r(b"PDFAnnotation", b"hasComb", {"retval": {"type": "Z"}})
    r(b"PDFAnnotation", b"isHighlighted", {"retval": {"type": b"Z"}})
    r(b"PDFAnnotation", b"isListChoice", {"retval": {"type": b"Z"}})
    r(b"PDFAnnotation", b"isMultiline", {"retval": {"type": b"Z"}})
    r(b"PDFAnnotation", b"isOpen", {"retval": {"type": b"Z"}})
    r(b"PDFAnnotation", b"isPasswordField", {"retval": {"type": "Z"}})
    r(b"PDFAnnotation", b"isReadOnly", {"retval": {"type": b"Z"}})
    r(b"PDFAnnotation", b"isSignature", {"retval": {"type": "Z"}})
    r(b"PDFAnnotation", b"radiosInUnison", {"retval": {"type": "Z"}})
    r(b"PDFAnnotation", b"setAllowsToggleToOff:", {"arguments": {2: {"type": b"Z"}}})
    r(
        b"PDFAnnotation",
        b"setBoolean:forAnnotationKey:",
        {"retval": {"type": "Z"}, "arguments": {2: {"type": "Z"}}},
    )
    r(b"PDFAnnotation", b"setComb:", {"arguments": {2: {"type": b"Z"}}})
    r(b"PDFAnnotation", b"setHighlighted:", {"arguments": {2: {"type": "Z"}}})
    r(b"PDFAnnotation", b"setListChoice:", {"arguments": {2: {"type": b"Z"}}})
    r(b"PDFAnnotation", b"setMultiline:", {"arguments": {2: {"type": "Z"}}})
    r(b"PDFAnnotation", b"setOpen:", {"arguments": {2: {"type": b"Z"}}})
    r(b"PDFAnnotation", b"setRadiosInUnison:", {"arguments": {2: {"type": "Z"}}})
    r(b"PDFAnnotation", b"setReadOnly:", {"arguments": {2: {"type": b"Z"}}})
    r(b"PDFAnnotation", b"setRect:forAnnotationKey:", {"retval": {"type": "Z"}})
    r(b"PDFAnnotation", b"setShouldDisplay:", {"arguments": {2: {"type": b"Z"}}})
    r(b"PDFAnnotation", b"setShouldPrint:", {"arguments": {2: {"type": b"Z"}}})
    r(b"PDFAnnotation", b"setValue:forAnnotationKey:", {"retval": {"type": "Z"}})
    r(b"PDFAnnotation", b"shouldDisplay", {"retval": {"type": b"Z"}})
    r(b"PDFAnnotation", b"shouldPrint", {"retval": {"type": b"Z"}})
    r(b"PDFAnnotationButtonWidget", b"allowsToggleToOff", {"retval": {"type": b"Z"}})
    r(b"PDFAnnotationButtonWidget", b"isHighlighted", {"retval": {"type": b"Z"}})
    r(
        b"PDFAnnotationButtonWidget",
        b"setAllowsToggleToOff:",
        {"arguments": {2: {"type": b"Z"}}},
    )
    r(
        b"PDFAnnotationButtonWidget",
        b"setHighlighted:",
        {"arguments": {2: {"type": b"Z"}}},
    )
    r(b"PDFAnnotationChoiceWidget", b"isListChoice", {"retval": {"type": b"Z"}})
    r(
        b"PDFAnnotationChoiceWidget",
        b"setIsListChoice:",
        {"arguments": {2: {"type": b"Z"}}},
    )
    r(b"PDFAnnotationLink", b"setHighlighted:", {"arguments": {2: {"type": b"Z"}}})
    r(b"PDFAnnotationPopup", b"isOpen", {"retval": {"type": b"Z"}})
    r(b"PDFAnnotationPopup", b"setIsOpen:", {"arguments": {2: {"type": b"Z"}}})
    r(b"PDFAnnotationStamp", b"isSignature", {"retval": {"type": "Z"}})
    r(b"PDFAnnotationTextWidget", b"isMultiline", {"retval": {"type": b"Z"}})
    r(
        b"PDFAnnotationTextWidget",
        b"setIsMultiline:",
        {"arguments": {2: {"type": b"Z"}}},
    )
    r(b"PDFDocument", b"allowsCommenting", {"retval": {"type": "Z"}})
    r(b"PDFDocument", b"allowsContentAccessibility", {"retval": {"type": "Z"}})
    r(b"PDFDocument", b"allowsCopying", {"retval": {"type": b"Z"}})
    r(b"PDFDocument", b"allowsDocumentAssembly", {"retval": {"type": "Z"}})
    r(b"PDFDocument", b"allowsDocumentChanges", {"retval": {"type": "Z"}})
    r(b"PDFDocument", b"allowsFormFieldEntry", {"retval": {"type": "Z"}})
    r(b"PDFDocument", b"allowsPrinting", {"retval": {"type": b"Z"}})
    r(b"PDFDocument", b"isEncrypted", {"retval": {"type": b"Z"}})
    r(b"PDFDocument", b"isFinding", {"retval": {"type": b"Z"}})
    r(b"PDFDocument", b"isLocked", {"retval": {"type": b"Z"}})
    r(
        b"PDFDocument",
        b"printOperationForPrintInfo:scalingMode:autoRotate:",
        {"arguments": {4: {"type": b"Z"}}},
    )
    r(b"PDFDocument", b"unlockWithPassword:", {"retval": {"type": b"Z"}})
    r(b"PDFDocument", b"writeToFile:", {"retval": {"type": b"Z"}})
    r(b"PDFDocument", b"writeToFile:withOptions:", {"retval": {"type": b"Z"}})
    r(b"PDFDocument", b"writeToURL:", {"retval": {"type": b"Z"}})
    r(b"PDFDocument", b"writeToURL:withOptions:", {"retval": {"type": b"Z"}})
    r(b"PDFOutline", b"isOpen", {"retval": {"type": b"Z"}})
    r(b"PDFOutline", b"setIsOpen:", {"arguments": {2: {"type": b"Z"}}})
    r(b"PDFPage", b"displaysAnnotations", {"retval": {"type": b"Z"}})
    r(b"PDFPage", b"setDisplaysAnnotations:", {"arguments": {2: {"type": b"Z"}}})
    r(b"PDFSelection", b"drawForPage:active:", {"arguments": {3: {"type": b"Z"}}})
    r(
        b"PDFSelection",
        b"drawForPage:withBox:active:",
        {"arguments": {4: {"type": b"Z"}}},
    )
    r(b"PDFThumbnailView", b"allowsDragging", {"retval": {"type": b"Z"}})
    r(b"PDFThumbnailView", b"allowsMultipleSelection", {"retval": {"type": b"Z"}})
    r(b"PDFThumbnailView", b"setAllowsDragging:", {"arguments": {2: {"type": b"Z"}}})
    r(
        b"PDFThumbnailView",
        b"setAllowsMultipleSelection:",
        {"arguments": {2: {"type": b"Z"}}},
    )
    r(b"PDFView", b"acceptsDraggedFiles", {"retval": {"type": "Z"}})
    r(b"PDFView", b"allowsDragging", {"retval": {"type": b"Z"}})
    r(b"PDFView", b"autoScales", {"retval": {"type": b"Z"}})
    r(b"PDFView", b"canGoBack", {"retval": {"type": b"Z"}})
    r(b"PDFView", b"canGoForward", {"retval": {"type": b"Z"}})
    r(b"PDFView", b"canGoToFirstPage", {"retval": {"type": b"Z"}})
    r(b"PDFView", b"canGoToLastPage", {"retval": {"type": b"Z"}})
    r(b"PDFView", b"canGoToNextPage", {"retval": {"type": b"Z"}})
    r(b"PDFView", b"canGoToPreviousPage", {"retval": {"type": b"Z"}})
    r(b"PDFView", b"canZoomIn", {"retval": {"type": b"Z"}})
    r(b"PDFView", b"canZoomOut", {"retval": {"type": b"Z"}})
    r(b"PDFView", b"displaysAsBook", {"retval": {"type": b"Z"}})
    r(b"PDFView", b"displaysPageBreaks", {"retval": {"type": b"Z"}})
    r(b"PDFView", b"displaysRTL", {"retval": {"type": "Z"}})
    r(b"PDFView", b"enableDataDetectors", {"retval": {"type": b"Z"}})
    r(b"PDFView", b"enablePageShadows:", {"arguments": {2: {"type": b"Z"}}})
    r(b"PDFView", b"pageForPoint:nearest:", {"arguments": {3: {"type": b"Z"}}})
    r(b"PDFView", b"pageShadowsEnabled", {"retval": {"type": b"Z"}})
    r(b"PDFView", b"printWithInfo:autoRotate:", {"arguments": {3: {"type": b"Z"}}})
    r(
        b"PDFView",
        b"printWithInfo:autoRotate:pageScaling:",
        {"arguments": {3: {"type": b"Z"}}},
    )
    r(b"PDFView", b"setAcceptsDraggedFiles:", {"arguments": {2: {"type": "Z"}}})
    r(b"PDFView", b"setAllowsDragging:", {"arguments": {2: {"type": b"Z"}}})
    r(b"PDFView", b"setAutoScales:", {"arguments": {2: {"type": b"Z"}}})
    r(b"PDFView", b"setCurrentSelection:animate:", {"arguments": {3: {"type": b"Z"}}})
    r(b"PDFView", b"setDisplaysAsBook:", {"arguments": {2: {"type": b"Z"}}})
    r(b"PDFView", b"setDisplaysPageBreaks:", {"arguments": {2: {"type": b"Z"}}})
    r(b"PDFView", b"setDisplaysRTL:", {"arguments": {2: {"type": "Z"}}})
    r(b"PDFView", b"setEnableDataDetectors:", {"arguments": {2: {"type": b"Z"}}})
    r(b"PDFView", b"setShouldAntiAlias:", {"arguments": {2: {"type": b"Z"}}})
    r(b"PDFView", b"shouldAntiAlias", {"retval": {"type": b"Z"}})
finally:
    objc._updatingMetadata(False)
protocols = {
    "PDFViewDelegate": objc.informal_protocol(
        "PDFViewDelegate",
        [
            objc.selector(
                None, b"PDFViewWillClickOnLink:withURL:", b"v@:@@", isRequired=False
            ),
            objc.selector(
                None, b"PDFViewOpenPDF:forRemoteGoToAction:", b"v@:@@", isRequired=False
            ),
            objc.selector(None, b"PDFViewPerformFind:", b"v@:@", isRequired=False),
            objc.selector(
                None,
                b"PDFViewWillChangeScaleFactor:toScale:",
                sel32or64(b"f@:@f", b"d@:@d"),
                isRequired=False,
            ),
            objc.selector(None, b"PDFViewPerformPrint:", b"v@:@", isRequired=False),
            objc.selector(None, b"PDFViewPrintJobTitle:", b"@@:@", isRequired=False),
            objc.selector(None, b"PDFViewPerformGoToPage:", b"v@:@", isRequired=False),
        ],
    ),
    "PDFDocumentDelegate": objc.informal_protocol(
        "PDFDocumentDelegate",
        [
            objc.selector(None, b"classForPage", b"#@:", isRequired=False),
            objc.selector(None, b"classForAnnotationClass:", b"#@:#", isRequired=False),
            objc.selector(None, b"didMatchString:", b"v@:@", isRequired=False),
        ],
    ),
    "PDFDocumentNotifications": objc.informal_protocol(
        "PDFDocumentNotifications",
        [
            objc.selector(None, b"documentDidFindMatch:", b"v@:@", isRequired=False),
            objc.selector(
                None, b"documentDidBeginPageFind:", b"v@:@", isRequired=False
            ),
            objc.selector(
                None, b"documentDidBeginDocumentFind:", b"v@:@", isRequired=False
            ),
            objc.selector(None, b"documentDidUnlock:", b"v@:@", isRequired=False),
            objc.selector(None, b"documentDidEndPageFind:", b"v@:@", isRequired=False),
            objc.selector(
                None, b"documentDidEndDocumentFind:", b"v@:@", isRequired=False
            ),
        ],
    ),
}
expressions = {}

# END OF FILE
