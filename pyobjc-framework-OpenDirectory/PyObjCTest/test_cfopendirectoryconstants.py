"""
Some simple tests to check that the framework is properly wrapped.
"""
import objc
import CFOpenDirectory

from PyObjCTools.TestSupport import *


class TestCFOpenDirectoryConstants(TestCase):
    def testConstants(self):
        self.assertIsInstance(CFOpenDirectory.kODSessionProxyAddress, unicode)
        self.assertIsInstance(CFOpenDirectory.kODSessionProxyPort, unicode)
        self.assertIsInstance(CFOpenDirectory.kODSessionProxyUsername, unicode)
        self.assertIsInstance(CFOpenDirectory.kODSessionProxyPassword, unicode)

        self.assertIsInstance(CFOpenDirectory.kODRecordTypeAttributeTypes, unicode)
        self.assertIsInstance(CFOpenDirectory.kODRecordTypeAFPServer, unicode)
        self.assertIsInstance(CFOpenDirectory.kODRecordTypeAliases, unicode)
        self.assertIsInstance(CFOpenDirectory.kODRecordTypeAugments, unicode)
        self.assertIsInstance(CFOpenDirectory.kODRecordTypeAutomount, unicode)
        self.assertIsInstance(CFOpenDirectory.kODRecordTypeAutomountMap, unicode)
        self.assertIsInstance(CFOpenDirectory.kODRecordTypeAutoServerSetup, unicode)
        self.assertIsInstance(CFOpenDirectory.kODRecordTypeBootp, unicode)
        self.assertIsInstance(
            CFOpenDirectory.kODRecordTypeCertificateAuthorities, unicode
        )
        self.assertIsInstance(CFOpenDirectory.kODRecordTypeComputerLists, unicode)
        self.assertIsInstance(CFOpenDirectory.kODRecordTypeComputerGroups, unicode)
        self.assertIsInstance(CFOpenDirectory.kODRecordTypeComputers, unicode)
        self.assertIsInstance(CFOpenDirectory.kODRecordTypeConfiguration, unicode)
        self.assertIsInstance(CFOpenDirectory.kODRecordTypeEthernets, unicode)
        self.assertIsInstance(CFOpenDirectory.kODRecordTypeFileMakerServers, unicode)
        self.assertIsInstance(CFOpenDirectory.kODRecordTypeFTPServer, unicode)
        self.assertIsInstance(CFOpenDirectory.kODRecordTypeGroups, unicode)
        self.assertIsInstance(CFOpenDirectory.kODRecordTypeHostServices, unicode)
        self.assertIsInstance(CFOpenDirectory.kODRecordTypeHosts, unicode)
        self.assertIsInstance(CFOpenDirectory.kODRecordTypeLDAPServer, unicode)
        self.assertIsInstance(CFOpenDirectory.kODRecordTypeLocations, unicode)
        self.assertIsInstance(CFOpenDirectory.kODRecordTypeMounts, unicode)
        self.assertIsInstance(CFOpenDirectory.kODRecordTypeNFS, unicode)
        self.assertIsInstance(CFOpenDirectory.kODRecordTypeNetDomains, unicode)
        self.assertIsInstance(CFOpenDirectory.kODRecordTypeNetGroups, unicode)
        self.assertIsInstance(CFOpenDirectory.kODRecordTypeNetworks, unicode)
        self.assertIsInstance(CFOpenDirectory.kODRecordTypePeople, unicode)
        self.assertIsInstance(CFOpenDirectory.kODRecordTypePresetComputers, unicode)
        self.assertIsInstance(
            CFOpenDirectory.kODRecordTypePresetComputerGroups, unicode
        )
        self.assertIsInstance(CFOpenDirectory.kODRecordTypePresetComputerLists, unicode)
        self.assertIsInstance(CFOpenDirectory.kODRecordTypePresetGroups, unicode)
        self.assertIsInstance(CFOpenDirectory.kODRecordTypePresetUsers, unicode)
        self.assertIsInstance(CFOpenDirectory.kODRecordTypePrintService, unicode)
        self.assertIsInstance(CFOpenDirectory.kODRecordTypePrintServiceUser, unicode)
        self.assertIsInstance(CFOpenDirectory.kODRecordTypePrinters, unicode)
        self.assertIsInstance(CFOpenDirectory.kODRecordTypeProtocols, unicode)
        self.assertIsInstance(CFOpenDirectory.kODRecordTypeQTSServer, unicode)
        self.assertIsInstance(CFOpenDirectory.kODRecordTypeRecordTypes, unicode)
        self.assertIsInstance(CFOpenDirectory.kODRecordTypeResources, unicode)
        self.assertIsInstance(CFOpenDirectory.kODRecordTypeRPC, unicode)
        self.assertIsInstance(CFOpenDirectory.kODRecordTypeSMBServer, unicode)
        self.assertIsInstance(CFOpenDirectory.kODRecordTypeServer, unicode)
        self.assertIsInstance(CFOpenDirectory.kODRecordTypeServices, unicode)
        self.assertIsInstance(CFOpenDirectory.kODRecordTypeSharePoints, unicode)
        self.assertIsInstance(CFOpenDirectory.kODRecordTypeUsers, unicode)
        self.assertIsInstance(CFOpenDirectory.kODRecordTypeWebServer, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeAllAttributes, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeStandardOnly, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeNativeOnly, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeAdminLimits, unicode)
        self.assertIsInstance(
            CFOpenDirectory.kODAttributeTypeAltSecurityIdentities, unicode
        )
        self.assertIsInstance(
            CFOpenDirectory.kODAttributeTypeAuthenticationHint, unicode
        )
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeAllTypes, unicode)
        self.assertIsInstance(
            CFOpenDirectory.kODAttributeTypeAuthorityRevocationList, unicode
        )
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeBirthday, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeCACertificate, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeCapacity, unicode)
        self.assertIsInstance(
            CFOpenDirectory.kODAttributeTypeCertificateRevocationList, unicode
        )
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeComment, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeContactGUID, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeContactPerson, unicode)
        self.assertIsInstance(
            CFOpenDirectory.kODAttributeTypeCreationTimestamp, unicode
        )
        self.assertIsInstance(
            CFOpenDirectory.kODAttributeTypeCrossCertificatePair, unicode
        )
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeDataStamp, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeFullName, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeDNSDomain, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeDNSNameServer, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeENetAddress, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeExpire, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeFirstName, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeGUID, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeHardwareUUID, unicode)
        self.assertIsInstance(
            CFOpenDirectory.kODAttributeTypeHomeDirectoryQuota, unicode
        )
        self.assertIsInstance(
            CFOpenDirectory.kODAttributeTypeHomeDirectorySoftQuota, unicode
        )
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeHomeLocOwner, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeInternetAlias, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeKDCConfigData, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeLastName, unicode)
        self.assertIsInstance(
            CFOpenDirectory.kODAttributeTypeLDAPSearchBaseSuffix, unicode
        )
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeLocation, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeMapGUID, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeMCXFlags, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeMCXSettings, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeMailAttribute, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeMetaAutomountMap, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeMiddleName, unicode)
        self.assertIsInstance(
            CFOpenDirectory.kODAttributeTypeModificationTimestamp, unicode
        )
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeNFSHomeDirectory, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeNote, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeOperatingSystem, unicode)
        self.assertIsInstance(
            CFOpenDirectory.kODAttributeTypeOperatingSystemVersion, unicode
        )
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeOwner, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeOwnerGUID, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypePassword, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypePasswordPlus, unicode)
        self.assertIsInstance(
            CFOpenDirectory.kODAttributeTypePasswordPolicyOptions, unicode
        )
        self.assertIsInstance(
            CFOpenDirectory.kODAttributeTypePasswordServerList, unicode
        )
        self.assertIsInstance(
            CFOpenDirectory.kODAttributeTypePasswordServerLocation, unicode
        )
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypePicture, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypePort, unicode)
        self.assertIsInstance(
            CFOpenDirectory.kODAttributeTypePresetUserIsAdmin, unicode
        )
        self.assertIsInstance(
            CFOpenDirectory.kODAttributeTypePrimaryComputerGUID, unicode
        )
        self.assertIsInstance(
            CFOpenDirectory.kODAttributeTypePrimaryComputerList, unicode
        )
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypePrimaryGroupID, unicode)
        self.assertIsInstance(
            CFOpenDirectory.kODAttributeTypePrinter1284DeviceID, unicode
        )
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypePrinterLPRHost, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypePrinterLPRQueue, unicode)
        self.assertIsInstance(
            CFOpenDirectory.kODAttributeTypePrinterMakeAndModel, unicode
        )
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypePrinterType, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypePrinterURI, unicode)
        self.assertIsInstance(
            CFOpenDirectory.kODAttributeTypePrinterXRISupported, unicode
        )
        self.assertIsInstance(
            CFOpenDirectory.kODAttributeTypePrintServiceInfoText, unicode
        )
        self.assertIsInstance(
            CFOpenDirectory.kODAttributeTypePrintServiceInfoXML, unicode
        )
        self.assertIsInstance(
            CFOpenDirectory.kODAttributeTypePrintServiceUserData, unicode
        )
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeRealUserID, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeRelativeDNPrefix, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeSMBAcctFlags, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeSMBGroupRID, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeSMBHome, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeSMBHomeDrive, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeSMBKickoffTime, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeSMBLogoffTime, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeSMBLogonTime, unicode)
        self.assertIsInstance(
            CFOpenDirectory.kODAttributeTypeSMBPrimaryGroupSID, unicode
        )
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeSMBPWDLastSet, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeSMBProfilePath, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeSMBRID, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeSMBScriptPath, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeSMBSID, unicode)
        self.assertIsInstance(
            CFOpenDirectory.kODAttributeTypeSMBUserWorkstations, unicode
        )
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeServiceType, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeSetupAdvertising, unicode)
        self.assertIsInstance(
            CFOpenDirectory.kODAttributeTypeSetupAutoRegister, unicode
        )
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeSetupLocation, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeSetupOccupation, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeTimeToLive, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeUniqueID, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeUserCertificate, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeUserPKCS12Data, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeUserShell, unicode)
        self.assertIsInstance(
            CFOpenDirectory.kODAttributeTypeUserSMIMECertificate, unicode
        )
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeVFSDumpFreq, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeVFSLinkDir, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeVFSPassNo, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeVFSType, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeWeblogURI, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeXMLPlist, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeProtocolNumber, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeRPCNumber, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeNetworkNumber, unicode)
        self.assertIsInstance(
            CFOpenDirectory.kODAttributeTypeAccessControlEntry, unicode
        )
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeAddressLine1, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeAddressLine2, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeAddressLine3, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeAreaCode, unicode)
        self.assertIsInstance(
            CFOpenDirectory.kODAttributeTypeAuthenticationAuthority, unicode
        )
        self.assertIsInstance(
            CFOpenDirectory.kODAttributeTypeAutomountInformation, unicode
        )
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeBootParams, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeBuilding, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeServicesLocator, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeCity, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeCompany, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeComputers, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeCountry, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeDepartment, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeDNSName, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeEMailAddress, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeEMailContacts, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeFaxNumber, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeGroup, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeGroupMembers, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeGroupMembership, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeGroupServices, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeHomePhoneNumber, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeHTML, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeHomeDirectory, unicode)
        self.assertIsInstance(
            CFOpenDirectory.kODAttributeTypeIMHandle, unicode, unicode
        )
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeIPAddress, unicode)
        self.assertIsInstance(
            CFOpenDirectory.kODAttributeTypeIPAddressAndENetAddress, unicode
        )
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeIPv6Address, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeJPEGPhoto, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeJobTitle, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeKDCAuthKey, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeKeywords, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeLDAPReadReplicas, unicode)
        self.assertIsInstance(
            CFOpenDirectory.kODAttributeTypeLDAPWriteReplicas, unicode
        )
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeMapCoordinates, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeMapURI, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeMIME, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeMobileNumber, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeNestedGroups, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeNetGroups, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeNickName, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeOrganizationInfo, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeOrganizationName, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypePagerNumber, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypePhoneContacts, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypePhoneNumber, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypePGPPublicKey, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypePostalAddress, unicode)
        self.assertIsInstance(
            CFOpenDirectory.kODAttributeTypePostalAddressContacts, unicode
        )
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypePostalCode, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeNamePrefix, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeProtocols, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeRecordName, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeRelationships, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeResourceInfo, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeResourceType, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeState, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeStreet, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeNameSuffix, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeURL, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeVFSOpts, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeAlias, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeAuthCredential, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeCopyTimestamp, unicode)
        self.assertIsInstance(
            CFOpenDirectory.kODAttributeTypeDateRecordCreated, unicode
        )
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeKerberosRealm, unicode)
        self.assertIsInstance(
            CFOpenDirectory.kODAttributeTypeNTDomainComputerAccount, unicode
        )
        self.assertIsInstance(
            CFOpenDirectory.kODAttributeTypeOriginalHomeDirectory, unicode
        )
        self.assertIsInstance(
            CFOpenDirectory.kODAttributeTypeOriginalNFSHomeDirectory, unicode
        )
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeOriginalNodeName, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypePrimaryNTDomain, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypePwdAgingPolicy, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeReadOnlyNode, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeTimePackage, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeTotalSize, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeAuthMethod, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeMetaNodeLocation, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeNodePath, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypePlugInInfo, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeRecordType, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeSchema, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeSubNodes, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeNetGroupTriplet, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeSearchPath, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeSearchPolicy, unicode)
        self.assertIsInstance(
            CFOpenDirectory.kODAttributeTypeAutomaticSearchPath, unicode
        )
        self.assertIsInstance(
            CFOpenDirectory.kODAttributeTypeLocalOnlySearchPath, unicode
        )
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeCustomSearchPath, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeBuildVersion, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeConfigAvailable, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeConfigFile, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeCoreFWVersion, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeFunctionalState, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeFWVersion, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypePluginIndex, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeNumTableList, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeVersion, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypePIDValue, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeProcessName, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeTotalRefCount, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeDirRefCount, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeNodeRefCount, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeRecRefCount, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeAttrListRefCount, unicode)
        self.assertIsInstance(
            CFOpenDirectory.kODAttributeTypeAttrListValueRefCount, unicode
        )
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeDirRefs, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeNodeRefs, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeRecRefs, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeAttrListRefs, unicode)
        self.assertIsInstance(
            CFOpenDirectory.kODAttributeTypeAttrListValueRefs, unicode
        )
        self.assertIsInstance(CFOpenDirectory.kODAuthenticationType2WayRandom, unicode)
        self.assertIsInstance(
            CFOpenDirectory.kODAuthenticationType2WayRandomChangePasswd, unicode
        )
        self.assertIsInstance(CFOpenDirectory.kODAuthenticationTypeAPOP, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAuthenticationTypeCRAM_MD5, unicode)
        self.assertIsInstance(
            CFOpenDirectory.kODAuthenticationTypeChangePasswd, unicode
        )
        self.assertIsInstance(CFOpenDirectory.kODAuthenticationTypeClearText, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAuthenticationTypeCrypt, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAuthenticationTypeDIGEST_MD5, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAuthenticationTypeDeleteUser, unicode)
        self.assertIsInstance(
            CFOpenDirectory.kODAuthenticationTypeGetEffectivePolicy, unicode
        )
        self.assertIsInstance(
            CFOpenDirectory.kODAuthenticationTypeGetGlobalPolicy, unicode
        )
        self.assertIsInstance(
            CFOpenDirectory.kODAuthenticationTypeGetKerberosPrincipal, unicode
        )
        self.assertIsInstance(CFOpenDirectory.kODAuthenticationTypeGetPolicy, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAuthenticationTypeGetUserData, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAuthenticationTypeGetUserName, unicode)
        self.assertIsInstance(
            CFOpenDirectory.kODAuthenticationTypeKerberosTickets, unicode
        )
        self.assertIsInstance(
            CFOpenDirectory.kODAuthenticationTypeMPPEMasterKeys, unicode
        )
        self.assertIsInstance(CFOpenDirectory.kODAuthenticationTypeMSCHAP2, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAuthenticationTypeNTLMv2, unicode)
        self.assertIsInstance(
            CFOpenDirectory.kODAuthenticationTypeNTLMv2WithSessionKey, unicode
        )
        self.assertIsInstance(CFOpenDirectory.kODAuthenticationTypeNewUser, unicode)
        self.assertIsInstance(
            CFOpenDirectory.kODAuthenticationTypeNewUserWithPolicy, unicode
        )
        self.assertIsInstance(
            CFOpenDirectory.kODAuthenticationTypeNodeNativeClearTextOK, unicode
        )
        self.assertIsInstance(
            CFOpenDirectory.kODAuthenticationTypeNodeNativeNoClearText, unicode
        )
        self.assertIsInstance(
            CFOpenDirectory.kODAuthenticationTypeReadSecureHash, unicode
        )
        self.assertIsInstance(
            CFOpenDirectory.kODAuthenticationTypeSMBNTv2UserSessionKey, unicode
        )
        self.assertIsInstance(
            CFOpenDirectory.kODAuthenticationTypeSMBWorkstationCredentialSessionKey,
            unicode,
        )
        self.assertIsInstance(CFOpenDirectory.kODAuthenticationTypeSMB_LM_Key, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAuthenticationTypeSMB_NT_Key, unicode)
        self.assertIsInstance(
            CFOpenDirectory.kODAuthenticationTypeSMB_NT_UserSessionKey, unicode
        )
        self.assertIsInstance(
            CFOpenDirectory.kODAuthenticationTypeSMB_NT_WithUserSessionKey, unicode
        )
        self.assertIsInstance(
            CFOpenDirectory.kODAuthenticationTypeSetGlobalPolicy, unicode
        )
        self.assertIsInstance(CFOpenDirectory.kODAuthenticationTypeSetLMHash, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAuthenticationTypeSetNTHash, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAuthenticationTypeSetPassword, unicode)
        self.assertIsInstance(
            CFOpenDirectory.kODAuthenticationTypeSetPasswordAsCurrent, unicode
        )
        self.assertIsInstance(CFOpenDirectory.kODAuthenticationTypeSetPolicy, unicode)
        self.assertIsInstance(
            CFOpenDirectory.kODAuthenticationTypeSetPolicyAsCurrent, unicode
        )
        self.assertIsInstance(CFOpenDirectory.kODAuthenticationTypeSetUserData, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAuthenticationTypeSetUserName, unicode)
        self.assertIsInstance(
            CFOpenDirectory.kODAuthenticationTypeSetWorkstationPassword, unicode
        )
        self.assertIsInstance(
            CFOpenDirectory.kODAuthenticationTypeWithAuthorizationRef, unicode
        )
        self.assertIsInstance(
            CFOpenDirectory.kODAuthenticationTypeWriteSecureHash, unicode
        )

        self.assertEqual(CFOpenDirectory.kODNodeTypeAuthentication, 0x2201)
        self.assertEqual(CFOpenDirectory.kODNodeTypeContacts, 0x2204)
        self.assertEqual(CFOpenDirectory.kODNodeTypeNetwork, 0x2205)
        self.assertEqual(CFOpenDirectory.kODNodeTypeLocalNodes, 0x2200)
        self.assertEqual(CFOpenDirectory.kODNodeTypeConfigure, 0x2202)
        self.assertEqual(CFOpenDirectory.kODMatchAny, 0x0001)
        self.assertEqual(CFOpenDirectory.kODMatchEqualTo, 0x2001)
        self.assertEqual(CFOpenDirectory.kODMatchBeginsWith, 0x2002)
        self.assertEqual(CFOpenDirectory.kODMatchContains, 0x2004)
        self.assertEqual(CFOpenDirectory.kODMatchEndsWith, 0x2003)
        self.assertEqual(CFOpenDirectory.kODMatchInsensitiveEqualTo, 0x2101)
        self.assertEqual(CFOpenDirectory.kODMatchInsensitiveBeginsWith, 0x2102)
        self.assertEqual(CFOpenDirectory.kODMatchInsensitiveContains, 0x2104)
        self.assertEqual(CFOpenDirectory.kODMatchInsensitiveEndsWith, 0x2103)
        self.assertEqual(CFOpenDirectory.kODMatchGreaterThan, 0x2006)
        self.assertEqual(CFOpenDirectory.kODMatchLessThan, 0x2007)
        self.assertEqual(CFOpenDirectory.kODErrorSuccess, 0)
        self.assertEqual(CFOpenDirectory.kODErrorSessionLocalOnlyDaemonInUse, 1000)
        self.assertEqual(CFOpenDirectory.kODErrorSessionNormalDaemonInUse, 1001)
        self.assertEqual(CFOpenDirectory.kODErrorSessionDaemonNotRunning, 1002)
        self.assertEqual(CFOpenDirectory.kODErrorSessionDaemonRefused, 1003)
        self.assertEqual(CFOpenDirectory.kODErrorSessionProxyCommunicationError, 1100)
        self.assertEqual(CFOpenDirectory.kODErrorSessionProxyVersionMismatch, 1101)
        self.assertEqual(CFOpenDirectory.kODErrorSessionProxyIPUnreachable, 1102)
        self.assertEqual(CFOpenDirectory.kODErrorSessionProxyUnknownHost, 1103)
        self.assertEqual(CFOpenDirectory.kODErrorNodeUnknownName, 2000)
        self.assertEqual(CFOpenDirectory.kODErrorNodeUnknownType, 2001)
        self.assertEqual(CFOpenDirectory.kODErrorNodeDisabled, 2002)
        self.assertEqual(CFOpenDirectory.kODErrorNodeConnectionFailed, 2100)
        self.assertEqual(CFOpenDirectory.kODErrorNodeUnknownHost, 2200)
        self.assertEqual(CFOpenDirectory.kODErrorQuerySynchronize, 3000)
        self.assertEqual(CFOpenDirectory.kODErrorQueryInvalidMatchType, 3100)
        self.assertEqual(CFOpenDirectory.kODErrorQueryUnsupportedMatchType, 3101)
        self.assertEqual(CFOpenDirectory.kODErrorQueryTimeout, 3102)
        self.assertEqual(CFOpenDirectory.kODErrorRecordReadOnlyNode, 4000)
        self.assertEqual(CFOpenDirectory.kODErrorRecordPermissionError, 4001)
        self.assertEqual(CFOpenDirectory.kODErrorRecordParameterError, 4100)
        self.assertEqual(CFOpenDirectory.kODErrorRecordInvalidType, 4101)
        self.assertEqual(CFOpenDirectory.kODErrorRecordAlreadyExists, 4102)
        self.assertEqual(CFOpenDirectory.kODErrorRecordTypeDisabled, 4103)
        self.assertEqual(CFOpenDirectory.kODErrorRecordNoLongerExists, 4104)
        self.assertEqual(CFOpenDirectory.kODErrorRecordAttributeUnknownType, 4200)
        self.assertEqual(CFOpenDirectory.kODErrorRecordAttributeNotFound, 4201)
        self.assertEqual(CFOpenDirectory.kODErrorRecordAttributeValueSchemaError, 4202)
        self.assertEqual(CFOpenDirectory.kODErrorRecordAttributeValueNotFound, 4203)
        self.assertEqual(CFOpenDirectory.kODErrorCredentialsInvalid, 5000)
        self.assertEqual(CFOpenDirectory.kODErrorCredentialsMethodNotSupported, 5100)
        self.assertEqual(CFOpenDirectory.kODErrorCredentialsNotAuthorized, 5101)
        self.assertEqual(CFOpenDirectory.kODErrorCredentialsParameterError, 5102)
        self.assertEqual(CFOpenDirectory.kODErrorCredentialsOperationFailed, 5103)
        self.assertEqual(CFOpenDirectory.kODErrorCredentialsServerUnreachable, 5200)
        self.assertEqual(CFOpenDirectory.kODErrorCredentialsServerNotFound, 5201)
        self.assertEqual(CFOpenDirectory.kODErrorCredentialsServerError, 5202)
        self.assertEqual(CFOpenDirectory.kODErrorCredentialsServerTimeout, 5203)
        self.assertEqual(CFOpenDirectory.kODErrorCredentialsContactMaster, 5204)
        self.assertEqual(
            CFOpenDirectory.kODErrorCredentialsServerCommunicationError, 5205
        )
        self.assertEqual(CFOpenDirectory.kODErrorCredentialsAccountNotFound, 5300)
        self.assertEqual(CFOpenDirectory.kODErrorCredentialsAccountDisabled, 5301)
        self.assertEqual(CFOpenDirectory.kODErrorCredentialsAccountExpired, 5302)
        self.assertEqual(CFOpenDirectory.kODErrorCredentialsAccountInactive, 5303)
        self.assertEqual(
            CFOpenDirectory.kODErrorCredentialsAccountTemporarilyLocked, 5304
        )
        self.assertEqual(CFOpenDirectory.kODErrorCredentialsAccountLocked, 5305)
        self.assertEqual(CFOpenDirectory.kODErrorCredentialsPasswordExpired, 5400)
        self.assertEqual(
            CFOpenDirectory.kODErrorCredentialsPasswordChangeRequired, 5401
        )
        self.assertEqual(CFOpenDirectory.kODErrorCredentialsPasswordQualityFailed, 5402)
        self.assertEqual(CFOpenDirectory.kODErrorCredentialsPasswordTooShort, 5403)
        self.assertEqual(CFOpenDirectory.kODErrorCredentialsPasswordTooLong, 5404)
        self.assertEqual(CFOpenDirectory.kODErrorCredentialsPasswordNeedsLetter, 5405)
        self.assertEqual(CFOpenDirectory.kODErrorCredentialsPasswordNeedsDigit, 5406)
        self.assertEqual(CFOpenDirectory.kODErrorCredentialsPasswordChangeTooSoon, 5407)
        self.assertEqual(CFOpenDirectory.kODErrorCredentialsPasswordUnrecoverable, 5408)
        self.assertEqual(CFOpenDirectory.kODErrorCredentialsInvalidLogonHours, 5500)
        self.assertEqual(CFOpenDirectory.kODErrorCredentialsInvalidComputer, 5501)
        self.assertEqual(CFOpenDirectory.kODErrorPluginOperationNotSupported, 10000)
        self.assertEqual(CFOpenDirectory.kODErrorPluginError, 10001)
        self.assertEqual(CFOpenDirectory.kODErrorDaemonError, 10002)
        self.assertEqual(CFOpenDirectory.kODErrorPluginOperationTimeout, 10003)
        self.assertEqual(CFOpenDirectory.kODErrorPolicyUnsupported, 6000)
        self.assertEqual(CFOpenDirectory.kODErrorPolicyOutOfRange, 6001)
        self.assertIsInstance(CFOpenDirectory.kODAuthenticationTypeSecureHash, unicode)

    @min_os_level("10.7")
    def testConstants10_7(self):
        self.assertIsInstance(
            CFOpenDirectory.kODAttributeTypeMetaAmbiguousName, unicode
        )
        self.assertIsInstance(
            CFOpenDirectory.kODAttributeTypeMetaAugmentedAttributes, unicode
        )
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeMetaRecordName, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeKerberosServices, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeTrustInformation, unicode)

        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeNodeOptions, unicode)
        self.assertIsInstance(
            CFOpenDirectory.kODAttributeTypeAdvertisedServices, unicode
        )
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeLocaleRelay, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeLocaleSubnets, unicode)
        self.assertIsInstance(
            CFOpenDirectory.kODAttributeTypeNetworkInterfaces, unicode
        )
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeParentLocales, unicode)
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypePrimaryLocale, unicode)

    @expectedFailure
    @min_os_level("10.7")
    def testConstants10_7_missing(self):
        self.assertIsInstance(
            CFOpenDirectory.kODAuthenticationTypeSetCertificateHashAsCurrent, unicode
        )

    @min_os_level("10.8")
    def testConstants10_8(self):
        self.assertIsInstance(
            CFOpenDirectory.kODNodeOptionsQuerySkippedSubnode, unicode
        )
        self.assertIsInstance(CFOpenDirectory.kODRecordTypeQueryInformation, unicode)

    @min_os_level("10.11")
    def testConstants10_9_missing(self):
        # Constants declared in headers, but missing on the system. Radar #19360668
        # Available on OSX 10.11
        self.assertIsInstance(
            CFOpenDirectory.kODModuleConfigOptionQueryTimeout, unicode
        )
        self.assertIsInstance(
            CFOpenDirectory.kODModuleConfigOptionConnectionSetupTimeout, unicode
        )
        self.assertIsInstance(
            CFOpenDirectory.kODModuleConfigOptionConnectionIdleDisconnect, unicode
        )
        self.assertIsInstance(
            CFOpenDirectory.kODModuleConfigOptionPacketSigning, unicode
        )
        self.assertIsInstance(
            CFOpenDirectory.kODModuleConfigOptionPacketSigning, unicode
        )
        self.assertIsInstance(
            CFOpenDirectory.kODModuleConfigOptionPacketEncryption, unicode
        )
        self.assertIsInstance(
            CFOpenDirectory.kODModuleConfigOptionManInTheMiddle, unicode
        )
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeNodeSASLRealm, unicode)

    @min_os_level("10.9")
    def testConstants10_9(self):
        self.assertIsInstance(CFOpenDirectory.kODAttributeTypeProfiles, unicode)
        self.assertIsInstance(
            CFOpenDirectory.kODAttributeTypeProfilesTimestamp, unicode
        )
        self.assertIsInstance(
            CFOpenDirectory.kODPolicyTypePasswordCannotBeAccountName, unicode
        )
        self.assertIsInstance(
            CFOpenDirectory.kODPolicyTypePasswordChangeRequired, unicode
        )
        self.assertIsInstance(CFOpenDirectory.kODPolicyTypePasswordHistory, unicode)
        self.assertIsInstance(
            CFOpenDirectory.kODPolicyTypePasswordMinimumNumberOfCharacters, unicode
        )
        self.assertIsInstance(
            CFOpenDirectory.kODPolicyTypePasswordMaximumNumberOfCharacters, unicode
        )
        self.assertIsInstance(
            CFOpenDirectory.kODPolicyTypePasswordMaximumAgeInMinutes, unicode
        )
        self.assertIsInstance(
            CFOpenDirectory.kODPolicyTypePasswordRequiresAlpha, unicode
        )
        self.assertIsInstance(
            CFOpenDirectory.kODPolicyTypePasswordRequiresMixedCase, unicode
        )
        self.assertIsInstance(
            CFOpenDirectory.kODPolicyTypePasswordRequiresNumeric, unicode
        )
        self.assertIsInstance(
            CFOpenDirectory.kODPolicyTypePasswordRequiresSymbol, unicode
        )
        self.assertIsInstance(
            CFOpenDirectory.kODPolicyTypePasswordSelfModification, unicode
        )
        self.assertIsInstance(
            CFOpenDirectory.kODPolicyTypeAccountExpiresOnDate, unicode
        )
        self.assertIsInstance(
            CFOpenDirectory.kODPolicyTypeAccountMaximumFailedLogins, unicode
        )
        self.assertIsInstance(
            CFOpenDirectory.kODPolicyTypeAccountMaximumMinutesOfNonUse, unicode
        )

        self.assertEqual(CFOpenDirectory.kODExpirationTimeExpired, 0)
        self.assertEqual(CFOpenDirectory.kODExpirationTimeNeverExpires, -1)

    @expectedFailureIf(os_release().rsplit(".", 1)[0] in ("10.9", "10.10"))
    @min_os_level("10.9")
    def testConstants10_9_missing(self):
        self.assertIsInstance(
            CFOpenDirectory.kODPolicyTypeAccountMaximumMinutesUntilDisabled, unicode
        )
        self.assertIsInstance(
            CFOpenDirectory.kODPolicyTypeAccountMinutesUntilFailedLoginReset, unicode
        )

    @min_os_level("10.10")
    def testConstants10_10(self):
        self.assertIsInstance(CFOpenDirectory.kODPolicyKeyIdentifier, unicode)
        self.assertIsInstance(CFOpenDirectory.kODPolicyKeyParameters, unicode)
        self.assertIsInstance(CFOpenDirectory.kODPolicyKeyContent, unicode)
        self.assertIsInstance(CFOpenDirectory.kODPolicyCategoryAuthentication, unicode)
        self.assertIsInstance(CFOpenDirectory.kODPolicyCategoryPasswordContent, unicode)
        self.assertIsInstance(CFOpenDirectory.kODPolicyCategoryPasswordChange, unicode)
        self.assertIsInstance(CFOpenDirectory.kODPolicyAttributeRecordName, unicode)
        self.assertIsInstance(CFOpenDirectory.kODPolicyAttributeRecordType, unicode)
        self.assertIsInstance(CFOpenDirectory.kODPolicyAttributePassword, unicode)
        self.assertIsInstance(CFOpenDirectory.kODPolicyAttributePasswordHashes, unicode)
        self.assertIsInstance(
            CFOpenDirectory.kODPolicyAttributePasswordHistory, unicode
        )
        self.assertIsInstance(
            CFOpenDirectory.kODPolicyAttributePasswordHistoryDepth, unicode
        )
        self.assertIsInstance(CFOpenDirectory.kODPolicyAttributeCurrentDate, unicode)
        self.assertIsInstance(CFOpenDirectory.kODPolicyAttributeCurrentTime, unicode)
        self.assertIsInstance(
            CFOpenDirectory.kODPolicyAttributeCurrentTimeOfDay, unicode
        )
        self.assertIsInstance(
            CFOpenDirectory.kODPolicyAttributeCurrentDayOfWeek, unicode
        )
        self.assertIsInstance(
            CFOpenDirectory.kODPolicyAttributeFailedAuthentications, unicode
        )
        self.assertIsInstance(
            CFOpenDirectory.kODPolicyAttributeMaximumFailedAuthentications, unicode
        )
        self.assertIsInstance(
            CFOpenDirectory.kODPolicyAttributeLastFailedAuthenticationTime, unicode
        )
        self.assertIsInstance(
            CFOpenDirectory.kODPolicyAttributeLastAuthenticationTime, unicode
        )
        self.assertIsInstance(
            CFOpenDirectory.kODPolicyAttributeLastPasswordChangeTime, unicode
        )
        self.assertIsInstance(
            CFOpenDirectory.kODPolicyAttributeNewPasswordRequiredTime, unicode
        )
        self.assertIsInstance(CFOpenDirectory.kODPolicyAttributeCreationTime, unicode)
        self.assertIsInstance(
            CFOpenDirectory.kODPolicyAttributeExpiresEveryNDays, unicode
        )
        self.assertIsInstance(CFOpenDirectory.kODPolicyAttributeEnableOnDate, unicode)
        self.assertIsInstance(CFOpenDirectory.kODPolicyAttributeExpiresOnDate, unicode)
        self.assertIsInstance(
            CFOpenDirectory.kODPolicyAttributeEnableOnDayOfWeek, unicode
        )
        self.assertIsInstance(
            CFOpenDirectory.kODPolicyAttributeExpiresOnDayOfWeek, unicode
        )
        self.assertIsInstance(
            CFOpenDirectory.kODPolicyAttributeEnableAtTimeOfDay, unicode
        )
        self.assertIsInstance(
            CFOpenDirectory.kODPolicyAttributeExpiresAtTimeOfDay, unicode
        )
        self.assertIsInstance(
            CFOpenDirectory.kODPolicyAttributeDaysUntilExpiration, unicode
        )

    @min_os_level("10.11")
    def testConstants10_11(self):
        self.assertIsInstance(CFOpenDirectory.kODPolicyKeyContentDescription, unicode)
        self.assertIsInstance(CFOpenDirectory.kODPolicyKeyEvaluationDetails, unicode)
        self.assertIsInstance(CFOpenDirectory.kODPolicyKeyPolicySatisfied, unicode)

    @expectedFailure
    @min_os_level("10.13")
    def testConstants10_13(self):
        # Not actually exported...
        self.assertIsInstance(
            CFOpenDirectory.kODAuthenticationTypeClearTextReadOnly, unicode
        )

    @min_os_level("10.15")
    def testConstants10_15(self):
        self.assertIsInstance(CFOpenDirectory.kODBackOffSeconds, unicode)


if __name__ == "__main__":
    main()
