import CoreServices
from PyObjCTools.TestSupport import TestCase


class TestPEFBinaryFormat(TestCase):
    def assert_not_wrapped(self, name):
        self.assertTrue(
            not hasattr(CoreServices, name), "%r exposed in bindings" % (name,)
        )

    def test_not_wrapped(self):
        self.assert_not_wrapped("IncludePEF2Declarations")
        self.assert_not_wrapped("kPEFRelocLgByImportMaxIndex")
        self.assert_not_wrapped("PEFContainerHeader")
        self.assert_not_wrapped("kPEFTag1")
        self.assert_not_wrapped("kPEFTag2")
        self.assert_not_wrapped("kPEFVersion")
        self.assert_not_wrapped("kPEFFirstSectionHeaderOffset")
        self.assert_not_wrapped("PEFFirstSectionNameOffset")
        self.assert_not_wrapped("PEFSectionHeader")
        self.assert_not_wrapped("kPEFCodeSection")
        self.assert_not_wrapped("kPEFUnpackedDataSection")
        self.assert_not_wrapped("kPEFPackedDataSection")
        self.assert_not_wrapped("kPEFConstantSection")
        self.assert_not_wrapped("kPEFExecDataSection")
        self.assert_not_wrapped("kPEFLoaderSection")
        self.assert_not_wrapped("kPEFDebugSection")
        self.assert_not_wrapped("kPEFExceptionSection")
        self.assert_not_wrapped("kPEFTracebackSection")
        self.assert_not_wrapped("kPEFProcessShare")
        self.assert_not_wrapped("kPEFGlobalShare")
        self.assert_not_wrapped("kPEFProtectedShare")
        self.assert_not_wrapped("kPEFPkDataZero")
        self.assert_not_wrapped("kPEFPkDataBlock")
        self.assert_not_wrapped("kPEFPkDataRepeat")
        self.assert_not_wrapped("kPEFPkDataRepeatBlock")
        self.assert_not_wrapped("kPEFPkDataRepeatZero")
        self.assert_not_wrapped("kPEFPkDataOpcodeShift")
        self.assert_not_wrapped("kPEFPkDataCount5Mask")
        self.assert_not_wrapped("kPEFPkDataMaxCount5")
        self.assert_not_wrapped("kPEFPkDataVCountShift")
        self.assert_not_wrapped("kPEFPkDataVCountMask")
        self.assert_not_wrapped("kPEFPkDataVCountEndMask")
        self.assert_not_wrapped("PEFPkDataOpcode")
        self.assert_not_wrapped("PEFPkDataCount5")
        self.assert_not_wrapped("PEFPkDataComposeInstr")
        self.assert_not_wrapped("PEFLoaderInfoHeader")
        self.assert_not_wrapped("PEFImportedLibrary")
        self.assert_not_wrapped("kPEFWeakImportLibMask")
        self.assert_not_wrapped("kPEFInitLibBeforeMask")
        self.assert_not_wrapped("PEFImportedSymbol")
        self.assert_not_wrapped("kPEFImpSymClassShift")
        self.assert_not_wrapped("kPEFImpSymNameOffsetMask")
        self.assert_not_wrapped("kPEFImpSymMaxNameOffset")
        self.assert_not_wrapped("PEFImportedSymbolClass")
        self.assert_not_wrapped("PEFImportedSymbolNameOffset")
        self.assert_not_wrapped("PEFComposeImportedSymbol")
        self.assert_not_wrapped("kPEFCodeSymbol")
        self.assert_not_wrapped("kPEFDataSymbol")
        self.assert_not_wrapped("kPEFTVectorSymbol")
        self.assert_not_wrapped("kPEFTOCSymbol")
        self.assert_not_wrapped("kPEFGlueSymbol")
        self.assert_not_wrapped("kPEFUndefinedSymbol")
        self.assert_not_wrapped("kPEFWeakImportSymMask")
        self.assert_not_wrapped("PEFExportedSymbolHashSlot")
        self.assert_not_wrapped("kPEFHashSlotSymCountShift")
        self.assert_not_wrapped("kPEFHashSlotFirstKeyMask")
        self.assert_not_wrapped("kPEFHashSlotMaxSymbolCount")
        self.assert_not_wrapped("kPEFHashSlotMaxKeyIndex")
        self.assert_not_wrapped("PEFHashTableIndex")
        self.assert_not_wrapped("PEFHashSlotSymbolCount")
        self.assert_not_wrapped("PEFHashSlotFirstKey")
        self.assert_not_wrapped("PEFComposeExportedSymbolHashSlot")
        self.assert_not_wrapped("PEFSplitHashWord")
        self.assert_not_wrapped("PEFExportedSymbolKey")
        self.assert_not_wrapped("kPEFHashLengthShift")
        self.assert_not_wrapped("kPEFHashValueMask")
        self.assert_not_wrapped("kPEFHashMaxLength")
        self.assert_not_wrapped("PEFHashNameLength")
        self.assert_not_wrapped("PEFHashValue")
        self.assert_not_wrapped("PEFComposeFullHashWord")
        self.assert_not_wrapped("PEFExportedSymbol")
        self.assert_not_wrapped("kPEFExpSymClassShift")
        self.assert_not_wrapped("kPEFExpSymNameOffsetMask")
        self.assert_not_wrapped("kPEFExpSymMaxNameOffset")
        self.assert_not_wrapped("PEFExportedSymbolClass")
        self.assert_not_wrapped("PEFExportedSymbolNameOffset")
        self.assert_not_wrapped("PEFComposeExportedSymbol")
        self.assert_not_wrapped("kPEFAbsoluteExport")
        self.assert_not_wrapped("kPEFReexportedImport")
        self.assert_not_wrapped("PEFLoaderRelocationHeader")
        self.assert_not_wrapped("PEFRFShift")
        self.assert_not_wrapped("PEFRFMask")
        self.assert_not_wrapped("PEFRelocField")
        self.assert_not_wrapped("kPEFRelocBasicOpcodeRange")
        self.assert_not_wrapped("PEFRelocBasicOpcode")
        self.assert_not_wrapped("kPEFRelocBySectDWithSkip")
        self.assert_not_wrapped("kPEFRelocBySectC")
        self.assert_not_wrapped("kPEFRelocBySectD")
        self.assert_not_wrapped("kPEFRelocTVector12")
        self.assert_not_wrapped("kPEFRelocTVector8")
        self.assert_not_wrapped("kPEFRelocVTable8")
        self.assert_not_wrapped("kPEFRelocImportRun")
        self.assert_not_wrapped("kPEFRelocSmByImport")
        self.assert_not_wrapped("kPEFRelocSmSetSectC")
        self.assert_not_wrapped("kPEFRelocSmSetSectD")
        self.assert_not_wrapped("kPEFRelocSmBySection")
        self.assert_not_wrapped("kPEFRelocIncrPosition")
        self.assert_not_wrapped("kPEFRelocSmRepeat")
        self.assert_not_wrapped("kPEFRelocSetPosition")
        self.assert_not_wrapped("kPEFRelocLgByImport")
        self.assert_not_wrapped("kPEFRelocLgRepeat")
        self.assert_not_wrapped("kPEFRelocLgSetOrBySection")
        self.assert_not_wrapped("kPEFRelocUndefinedOpcode")
        self.assert_not_wrapped("kPEFRelocLgBySectionSubopcode")
        self.assert_not_wrapped("kPEFRelocLgSetSectCSubopcode")
        self.assert_not_wrapped("kPEFRelocLgSetSectDSubopcode")
        self.assert_not_wrapped("PEFRelocLgSetOrBySubopcode")
        self.assert_not_wrapped("PEFMaskedBasicOpcodes")
        self.assert_not_wrapped("kPEFRelocWithSkipMaxSkipCount")
        self.assert_not_wrapped("kPEFRelocWithSkipMaxRelocCount")
        self.assert_not_wrapped("PEFRelocWithSkipSkipCount")
        self.assert_not_wrapped("PEFRelocWithSkipRelocCount")
        self.assert_not_wrapped("PEFRelocComposeWithSkip")
        self.assert_not_wrapped("kPEFRelocRunMaxRunLength")
        self.assert_not_wrapped("PEFRelocRunSubopcode")
        self.assert_not_wrapped("PEFRelocRunRunLength")
        self.assert_not_wrapped("PEFRelocComposeRun")
        self.assert_not_wrapped("PEFRelocComposeBySectC")
        self.assert_not_wrapped("PEFRelocComposeBySectD")
        self.assert_not_wrapped("PEFRelocComposeTVector12")
        self.assert_not_wrapped("PEFRelocComposeTVector8")
        self.assert_not_wrapped("PEFRelocComposeVTable8")
        self.assert_not_wrapped("PEFRelocComposeImportRun")
        self.assert_not_wrapped("kPEFRelocSmIndexMaxIndex")
        self.assert_not_wrapped("PEFRelocSmIndexSubopcode")
        self.assert_not_wrapped("PEFRelocSmIndexIndex")
        self.assert_not_wrapped("PEFRelocComposeSmIndex")
        self.assert_not_wrapped("PEFRelocComposeSmByImport")
        self.assert_not_wrapped("PEFRelocComposeSmSetSectC")
        self.assert_not_wrapped("PEFRelocComposeSmSetSectD")
        self.assert_not_wrapped("PEFRelocComposeSmBySection")
        self.assert_not_wrapped("kPEFRelocIncrPositionMaxOffset")
        self.assert_not_wrapped("PEFRelocIncrPositionOffset")
        self.assert_not_wrapped("PEFRelocComposeIncrPosition")
        self.assert_not_wrapped("kPEFRelocSmRepeatMaxChunkCount")
        self.assert_not_wrapped("kPEFRelocSmRepeatMaxRepeatCount")
        self.assert_not_wrapped("PEFRelocSmRepeatChunkCount")
        self.assert_not_wrapped("PEFRelocSmRepeatRepeatCount")
        self.assert_not_wrapped("PEFRelocComposeSmRepeat")
        self.assert_not_wrapped("kPEFRelocSetPosMaxOffset")
        self.assert_not_wrapped("PEFRelocSetPosOffsetHigh")
        self.assert_not_wrapped("PEFRelocSetPosFullOffset")
        self.assert_not_wrapped("PEFRelocComposeSetPosition_1st")
        self.assert_not_wrapped("PEFRelocComposeSetPosition_2nd")
        self.assert_not_wrapped("PEFRelocLgByImportIndexHigh")
        self.assert_not_wrapped("PEFRelocLgByImportFullIndex")
        self.assert_not_wrapped("PEFRelocComposeLgByImport_1st")
        self.assert_not_wrapped("PEFRelocComposeLgByImport_2nd")
        self.assert_not_wrapped("kPEFRelocLgRepeatMaxChunkCount")
        self.assert_not_wrapped("kPEFRelocLgRepeatMaxRepeatCount")
        self.assert_not_wrapped("PEFRelocLgRepeatChunkCount")
        self.assert_not_wrapped("PEFRelocLgRepeatRepeatCountHigh")
        self.assert_not_wrapped("PEFRelocLgRepeatFullRepeatCount")
        self.assert_not_wrapped("PEFRelocComposeLgRepeat_1st")
        self.assert_not_wrapped("PEFRelocComposeLgRepeat_2nd")
        self.assert_not_wrapped("kPEFRelocLgSetOrBySectionMaxIndex")
        self.assert_not_wrapped("PEFRelocLgSetOrBySectionSubopcode")
        self.assert_not_wrapped("PEFRelocLgSetOrBySectionIndexHigh")
        self.assert_not_wrapped("PEFRelocLgSetOrBySectionFullIndex")
        self.assert_not_wrapped("PEFRelocComposeLgSetOrBySection_1st")
        self.assert_not_wrapped("PEFRelocComposeLgSetOrBySection_2nd")
        self.assert_not_wrapped("PEFRelocComposeLgBySection")
        self.assert_not_wrapped("PEFRelocComposeLgSetSectC")
        self.assert_not_wrapped("PEFRelocComposeLgSetSectD")
        self.assert_not_wrapped("XLibContainerHeader")
        self.assert_not_wrapped("kXLibTag1")
        self.assert_not_wrapped("kVLibTag2")
        self.assert_not_wrapped("kBLibTag2")
        self.assert_not_wrapped("kXLibVersion")
        self.assert_not_wrapped("XLibExportedSymbolHashSlot")
        self.assert_not_wrapped("XLibExportedSymbolKey")
        self.assert_not_wrapped("XLibExportedSymbol")
        self.assert_not_wrapped("PEF2ContainerHeader")
        self.assert_not_wrapped("kPEF2Tag1")
        self.assert_not_wrapped("kPEF2Tag2")
        self.assert_not_wrapped("kPEF2CurrentFormat")
        self.assert_not_wrapped("kPEF2OldestHandler")
        self.assert_not_wrapped("kPEF2IsReexportLibraryMask")
        self.assert_not_wrapped("kPEF2IsGlueLibraryMask")
        self.assert_not_wrapped("kPEF2StringsAreASCII")
        self.assert_not_wrapped("kPEF2StringsAreUnicode")
        self.assert_not_wrapped("PEF2SectionHeader")
        self.assert_not_wrapped("kPEF2SectionHasCodeMask")
        self.assert_not_wrapped("kPEF2SectionIsWriteableMask")
        self.assert_not_wrapped("kPEF2SectionHasRelocationsMask")
        self.assert_not_wrapped("kPEF2SectionContentsArePackedMask")
        self.assert_not_wrapped("kPEF2SectionNoZeroFillMask")
        self.assert_not_wrapped("kPEF2SectionResidentMask")
        self.assert_not_wrapped("kPEF2SectionFollowsPriorMask")
        self.assert_not_wrapped("kPEF2SectionPrecedesNextMask")
        self.assert_not_wrapped("kPEF2SectionHasLoaderTablesMask")
        self.assert_not_wrapped("kPEF2SectionHasDebugTablesMask")
        self.assert_not_wrapped("kPEF2SectionHasExceptionTablesMask")
        self.assert_not_wrapped("kPEF2SectionHasTracebackTablesMask")
        self.assert_not_wrapped("kPEF2PrivateShare")
        self.assert_not_wrapped("kPEF2ProcessShare")
        self.assert_not_wrapped("kPEF2GlobalShare")
        self.assert_not_wrapped("kPEF2ProtectedShare")
        self.assert_not_wrapped("PEF2LoaderInfoHeader")
        self.assert_not_wrapped("kPEF2LdrInfoLargeImpSymMask")
        self.assert_not_wrapped("kPEF2LdrInfoLargeExpSymMask")
        self.assert_not_wrapped("kPEF2LdrInfoLargeExpHashMask")
        self.assert_not_wrapped("PEF2ImportedLibrary")
        self.assert_not_wrapped("kPEF2WeakImportLibMask")
        self.assert_not_wrapped("kPEF2InitLibBeforeMask")
        self.assert_not_wrapped("PEF2SmImportedSymbol")
        self.assert_not_wrapped("PEF2ComposeSmImportedSymbol")
        self.assert_not_wrapped("PEF2LgImportedSymbol")
        self.assert_not_wrapped("PEF2SmExportedSymbolHashSlot")
        self.assert_not_wrapped("PEF2ExportedSymbolKey")
        self.assert_not_wrapped("PEF2SmExportedSymbol")
        self.assert_not_wrapped("PEF2ComposeSmExportedSymbol")
        self.assert_not_wrapped("PEF2LgExportedSymbolHashSlot")
        self.assert_not_wrapped("PEF2LgExportedSymbol")
        self.assert_not_wrapped("PEF2LoaderRelocationHeader")
