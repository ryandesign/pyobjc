from PyObjCTools.TestSupport import *

import AVFoundation


class TestAVMetadataIdentifiers(TestCase):
    @min_os_level("10.10")
    def testConstants10(self):
        self.assertIsInstance(AVFoundation.AVMetadataCommonIdentifierTitle, unicode)
        self.assertIsInstance(AVFoundation.AVMetadataCommonIdentifierCreator, unicode)
        self.assertIsInstance(AVFoundation.AVMetadataCommonIdentifierSubject, unicode)
        self.assertIsInstance(
            AVFoundation.AVMetadataCommonIdentifierDescription, unicode
        )
        self.assertIsInstance(AVFoundation.AVMetadataCommonIdentifierPublisher, unicode)
        self.assertIsInstance(
            AVFoundation.AVMetadataCommonIdentifierContributor, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataCommonIdentifierCreationDate, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataCommonIdentifierLastModifiedDate, unicode
        )
        self.assertIsInstance(AVFoundation.AVMetadataCommonIdentifierType, unicode)
        self.assertIsInstance(AVFoundation.AVMetadataCommonIdentifierFormat, unicode)
        self.assertIsInstance(
            AVFoundation.AVMetadataCommonIdentifierAssetIdentifier, unicode
        )
        self.assertIsInstance(AVFoundation.AVMetadataCommonIdentifierSource, unicode)
        self.assertIsInstance(AVFoundation.AVMetadataCommonIdentifierLanguage, unicode)
        self.assertIsInstance(AVFoundation.AVMetadataCommonIdentifierRelation, unicode)
        self.assertIsInstance(AVFoundation.AVMetadataCommonIdentifierLocation, unicode)
        self.assertIsInstance(
            AVFoundation.AVMetadataCommonIdentifierCopyrights, unicode
        )
        self.assertIsInstance(AVFoundation.AVMetadataCommonIdentifierAlbumName, unicode)
        self.assertIsInstance(AVFoundation.AVMetadataCommonIdentifierAuthor, unicode)
        self.assertIsInstance(AVFoundation.AVMetadataCommonIdentifierArtist, unicode)
        self.assertIsInstance(AVFoundation.AVMetadataCommonIdentifierArtwork, unicode)
        self.assertIsInstance(AVFoundation.AVMetadataCommonIdentifierMake, unicode)
        self.assertIsInstance(AVFoundation.AVMetadataCommonIdentifierModel, unicode)
        self.assertIsInstance(AVFoundation.AVMetadataCommonIdentifierSoftware, unicode)
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeUserDataAlbum, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeUserDataArranger, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeUserDataArtist, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeUserDataAuthor, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeUserDataChapter, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeUserDataComment, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeUserDataComposer, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeUserDataCopyright, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeUserDataCreationDate, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeUserDataDescription, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeUserDataDirector, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeUserDataDisclaimer, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeUserDataEncodedBy, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeUserDataFullName, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeUserDataGenre, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeUserDataHostComputer, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeUserDataInformation, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeUserDataKeywords, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeUserDataMake, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeUserDataModel, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeUserDataOriginalArtist, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeUserDataOriginalFormat, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeUserDataOriginalSource, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeUserDataPerformers, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeUserDataProducer, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeUserDataPublisher, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeUserDataProduct, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeUserDataSoftware, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeUserDataSpecialPlaybackRequirements,
            unicode,
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeUserDataTrack, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeUserDataWarning, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeUserDataWriter, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeUserDataURLLink, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeUserDataLocationISO6709, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeUserDataTrackName, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeUserDataCredits, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeUserDataPhonogramRights, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeUserDataTaggedCharacteristic,
            unicode,
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierISOUserDataCopyright, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierISOUserDataTaggedCharacteristic, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifier3GPUserDataCopyright, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifier3GPUserDataAuthor, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifier3GPUserDataPerformer, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifier3GPUserDataGenre, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifier3GPUserDataRecordingYear, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifier3GPUserDataLocation, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifier3GPUserDataTitle, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifier3GPUserDataDescription, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifier3GPUserDataCollection, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifier3GPUserDataUserRating, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifier3GPUserDataThumbnail, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifier3GPUserDataAlbumAndTrack, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifier3GPUserDataKeywordList, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifier3GPUserDataMediaClassification, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifier3GPUserDataMediaRating, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeMetadataAuthor, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeMetadataComment, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeMetadataCopyright, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeMetadataCreationDate, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeMetadataDirector, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeMetadataDisplayName, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeMetadataInformation, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeMetadataKeywords, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeMetadataProducer, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeMetadataPublisher, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeMetadataAlbum, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeMetadataArtist, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeMetadataArtwork, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeMetadataDescription, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeMetadataSoftware, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeMetadataYear, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeMetadataGenre, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeMetadataiXML, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeMetadataLocationISO6709, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeMetadataMake, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeMetadataModel, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeMetadataArranger, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeMetadataEncodedBy, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeMetadataOriginalArtist, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeMetadataPerformer, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeMetadataComposer, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeMetadataCredits, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeMetadataPhonogramRights, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeMetadataCameraIdentifier, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeMetadataCameraFrameReadoutTime,
            unicode,
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeMetadataTitle, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeMetadataCollectionUser, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeMetadataRatingUser, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeMetadataLocationName, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeMetadataLocationBody, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeMetadataLocationNote, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeMetadataLocationRole, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeMetadataLocationDate, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeMetadataDirectionFacing, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeMetadataDirectionMotion, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeMetadataPreferredAffineTransform,
            unicode,
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifieriTunesMetadataAlbum, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifieriTunesMetadataArtist, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifieriTunesMetadataUserComment, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifieriTunesMetadataCoverArt, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifieriTunesMetadataCopyright, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifieriTunesMetadataReleaseDate, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifieriTunesMetadataEncodedBy, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifieriTunesMetadataPredefinedGenre, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifieriTunesMetadataUserGenre, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifieriTunesMetadataSongName, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifieriTunesMetadataTrackSubTitle, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifieriTunesMetadataEncodingTool, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifieriTunesMetadataComposer, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifieriTunesMetadataAlbumArtist, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifieriTunesMetadataAccountKind, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifieriTunesMetadataAppleID, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifieriTunesMetadataArtistID, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifieriTunesMetadataSongID, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifieriTunesMetadataDiscCompilation, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifieriTunesMetadataDiscNumber, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifieriTunesMetadataGenreID, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifieriTunesMetadataGrouping, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifieriTunesMetadataPlaylistID, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifieriTunesMetadataContentRating, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifieriTunesMetadataBeatsPerMin, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifieriTunesMetadataTrackNumber, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifieriTunesMetadataArtDirector, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifieriTunesMetadataArranger, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifieriTunesMetadataAuthor, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifieriTunesMetadataLyrics, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifieriTunesMetadataAcknowledgement, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifieriTunesMetadataConductor, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifieriTunesMetadataDescription, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifieriTunesMetadataDirector, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifieriTunesMetadataEQ, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifieriTunesMetadataLinerNotes, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifieriTunesMetadataRecordCompany, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifieriTunesMetadataOriginalArtist, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifieriTunesMetadataPhonogramRights, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifieriTunesMetadataProducer, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifieriTunesMetadataPerformer, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifieriTunesMetadataPublisher, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifieriTunesMetadataSoundEngineer, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifieriTunesMetadataSoloist, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifieriTunesMetadataCredits, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifieriTunesMetadataThanks, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifieriTunesMetadataOnlineExtras, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifieriTunesMetadataExecProducer, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataAudioEncryption, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataAttachedPicture, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataAudioSeekPointIndex, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataComments, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataEncryption, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataEqualization, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataEqualization2, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataEventTimingCodes, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataGeneralEncapsulatedObject,
            unicode,
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataGroupIdentifier, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataInvolvedPeopleList_v23, unicode
        )
        self.assertIsInstance(AVFoundation.AVMetadataIdentifierID3MetadataLink, unicode)
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataMusicCDIdentifier, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataMPEGLocationLookupTable, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataOwnership, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataPrivate, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataPlayCounter, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataPopularimeter, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataPositionSynchronization, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataRecommendedBufferSize, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataRelativeVolumeAdjustment,
            unicode,
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataRelativeVolumeAdjustment2,
            unicode,
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataReverb, unicode
        )
        self.assertIsInstance(AVFoundation.AVMetadataIdentifierID3MetadataSeek, unicode)
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataSignature, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataSynchronizedLyric, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataSynchronizedTempoCodes, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataAlbumTitle, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataBeatsPerMinute, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataComposer, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataContentType, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataCopyright, unicode
        )
        self.assertIsInstance(AVFoundation.AVMetadataIdentifierID3MetadataDate, unicode)
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataEncodingTime, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataPlaylistDelay, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataOriginalReleaseTime, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataRecordingTime, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataReleaseTime, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataTaggingTime, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataEncodedBy, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataLyricist, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataFileType, unicode
        )
        self.assertIsInstance(AVFoundation.AVMetadataIdentifierID3MetadataTime, unicode)
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataInvolvedPeopleList_v24, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataContentGroupDescription, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataTitleDescription, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataSubTitle, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataInitialKey, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataLanguage, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataLength, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataMusicianCreditsList, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataMediaType, unicode
        )
        self.assertIsInstance(AVFoundation.AVMetadataIdentifierID3MetadataMood, unicode)
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataOriginalAlbumTitle, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataOriginalFilename, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataOriginalLyricist, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataOriginalArtist, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataOriginalReleaseYear, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataFileOwner, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataLeadPerformer, unicode
        )
        self.assertIsInstance(AVFoundation.AVMetadataIdentifierID3MetadataBand, unicode)
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataConductor, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataModifiedBy, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataPartOfASet, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataProducedNotice, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataPublisher, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataTrackNumber, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataRecordingDates, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataInternetRadioStationName,
            unicode,
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataInternetRadioStationOwner,
            unicode,
        )
        self.assertIsInstance(AVFoundation.AVMetadataIdentifierID3MetadataSize, unicode)
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataAlbumSortOrder, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataPerformerSortOrder, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataTitleSortOrder, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataInternationalStandardRecordingCode,
            unicode,
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataEncodedWith, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataSetSubtitle, unicode
        )
        self.assertIsInstance(AVFoundation.AVMetadataIdentifierID3MetadataYear, unicode)
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataUserText, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataUniqueFileIdentifier, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataTermsOfUse, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataUnsynchronizedLyric, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataCommercialInformation, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataCopyrightInformation, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataOfficialAudioFileWebpage,
            unicode,
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataOfficialArtistWebpage, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataOfficialAudioSourceWebpage,
            unicode,
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataOfficialInternetRadioStationHomepage,
            unicode,
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataPayment, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataOfficialPublisherWebpage,
            unicode,
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataUserURL, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierIcyMetadataStreamTitle, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierIcyMetadataStreamURL, unicode
        )

    @min_os_level("10.11")
    def testConstants10_11(self):
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeMetadataDetectedFace, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeMetadataVideoOrientation, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierQuickTimeMetadataContentIdentifier, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataCommercial, unicode
        )
        self.assertIsInstance(
            AVFoundation.AVMetadataIdentifierID3MetadataCommerical, unicode
        )

    @min_os_level("10.12")
    def testConstants10_12(self):
        self.assertIsInstance(AVFoundation.AVMetadataIdentifierISOUserDataDate, unicode)

    @min_os_level("10.15")
    @expectedFailure
    def testConstants10_15(self):
        with self.subTest("humanbody"):
            self.assertIsInstance(
                AVFoundation.AVMetadataIdentifierQuickTimeMetadataDetectedHumanBody,
                unicode,
            )

        with self.subTest("catbody"):
            self.assertIsInstance(
                AVFoundation.AVMetadataIdentifierQuickTimeMetadataDetectedCatBody,
                unicode,
            )
        with self.subTest("dogbody"):
            self.assertIsInstance(
                AVFoundation.AVMetadataIdentifierQuickTimeMetadataDetectedDogBody,
                unicode,
            )
        with self.subTest("salientobject"):
            self.assertIsInstance(
                AVFoundation.AVMetadataIdentifierQuickTimeMetadataDetectedSalientObject,
                unicode,
            )
        with self.subTest("livephoto"):
            self.assertIsInstance(
                AVFoundation.AVMetadataIdentifierQuickTimeMetadataAutoLivePhoto, unicode
            )
        with self.subTest("vitalityscore"):
            self.assertIsInstance(
                AVFoundation.AVMetadataIdentifierQuickTimeMetadataLivePhotoVitalityScore,
                unicode,
            )
        with self.subTest("vitalityscoringversion"):
            self.assertIsInstance(
                AVFoundation.AVMetadataIdentifierQuickTimeMetadataLivePhotoVitalityScoringVersion,
                unicode,
            )
        with self.subTest("qualityscore"):
            self.assertIsInstance(
                AVFoundation.AVMetadataIdentifierQuickTimeMetadataSpatialOverCaptureQualityScore,
                unicode,
            )
        with self.subTest("qaulityscoringversion"):
            self.assertIsInstance(
                AVFoundation.AVMetadataIdentifierQuickTimeMetadataSpatialOverCaptureQualityScoringVersion,
                unicode,
            )


if __name__ == "__main__":
    main()
