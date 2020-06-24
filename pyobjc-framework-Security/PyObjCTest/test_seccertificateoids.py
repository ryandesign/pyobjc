import Security
from PyObjCTools.TestSupport import TestCase, min_os_level, expectedFailure


class TestSecCertificateOIDs(TestCase):
    def test_constants(self):
        self.assertIsInstance(Security.kSecOIDADC_CERT_POLICY, str)
        self.assertIsInstance(Security.kSecOIDAPPLE_CERT_POLICY, str)
        self.assertIsInstance(Security.kSecOIDAPPLE_EKU_CODE_SIGNING, str)
        self.assertIsInstance(Security.kSecOIDAPPLE_EKU_CODE_SIGNING_DEV, str)
        self.assertIsInstance(Security.kSecOIDAPPLE_EKU_ICHAT_ENCRYPTION, str)
        self.assertIsInstance(Security.kSecOIDAPPLE_EKU_ICHAT_SIGNING, str)
        self.assertIsInstance(Security.kSecOIDAPPLE_EKU_RESOURCE_SIGNING, str)
        self.assertIsInstance(Security.kSecOIDAPPLE_EKU_SYSTEM_IDENTITY, str)
        self.assertIsInstance(Security.kSecOIDAPPLE_EXTENSION, str)
        self.assertIsInstance(Security.kSecOIDAPPLE_EXTENSION_ADC_APPLE_SIGNING, str)
        self.assertIsInstance(Security.kSecOIDAPPLE_EXTENSION_ADC_DEV_SIGNING, str)
        self.assertIsInstance(Security.kSecOIDAPPLE_EXTENSION_APPLE_SIGNING, str)
        self.assertIsInstance(Security.kSecOIDAPPLE_EXTENSION_CODE_SIGNING, str)
        self.assertIsInstance(Security.kSecOIDAuthorityInfoAccess, str)
        self.assertIsInstance(Security.kSecOIDAuthorityKeyIdentifier, str)
        self.assertIsInstance(Security.kSecOIDBasicConstraints, str)
        self.assertIsInstance(Security.kSecOIDBiometricInfo, str)
        self.assertIsInstance(Security.kSecOIDCSSMKeyStruct, str)
        self.assertIsInstance(Security.kSecOIDCertIssuer, str)
        self.assertIsInstance(Security.kSecOIDCertificatePolicies, str)
        self.assertIsInstance(Security.kSecOIDClientAuth, str)
        self.assertIsInstance(Security.kSecOIDCollectiveStateProvinceName, str)
        self.assertIsInstance(Security.kSecOIDCollectiveStreetAddress, str)
        self.assertIsInstance(Security.kSecOIDCommonName, str)
        self.assertIsInstance(Security.kSecOIDCountryName, str)
        self.assertIsInstance(Security.kSecOIDCrlDistributionPoints, str)
        self.assertIsInstance(Security.kSecOIDCrlNumber, str)
        self.assertIsInstance(Security.kSecOIDCrlReason, str)
        self.assertIsInstance(Security.kSecOIDDOTMAC_CERT_EMAIL_ENCRYPT, str)
        self.assertIsInstance(Security.kSecOIDDOTMAC_CERT_EMAIL_SIGN, str)
        self.assertIsInstance(Security.kSecOIDDOTMAC_CERT_EXTENSION, str)
        self.assertIsInstance(Security.kSecOIDDOTMAC_CERT_IDENTITY, str)
        self.assertIsInstance(Security.kSecOIDDOTMAC_CERT_POLICY, str)
        self.assertIsInstance(Security.kSecOIDDeltaCrlIndicator, str)
        self.assertIsInstance(Security.kSecOIDDescription, str)
        self.assertIsInstance(Security.kSecOIDEKU_IPSec, str)
        self.assertIsInstance(Security.kSecOIDEmailAddress, str)
        self.assertIsInstance(Security.kSecOIDEmailProtection, str)
        self.assertIsInstance(Security.kSecOIDExtendedKeyUsage, str)
        self.assertIsInstance(Security.kSecOIDExtendedKeyUsageAny, str)
        self.assertIsInstance(Security.kSecOIDExtendedUseCodeSigning, str)
        self.assertIsInstance(Security.kSecOIDGivenName, str)
        self.assertIsInstance(Security.kSecOIDHoldInstructionCode, str)
        self.assertIsInstance(Security.kSecOIDInvalidityDate, str)
        self.assertIsInstance(Security.kSecOIDIssuerAltName, str)
        self.assertIsInstance(Security.kSecOIDIssuingDistributionPoint, str)
        self.assertIsInstance(Security.kSecOIDIssuingDistributionPoints, str)
        self.assertIsInstance(Security.kSecOIDKERBv5_PKINIT_KP_CLIENT_AUTH, str)
        self.assertIsInstance(Security.kSecOIDKERBv5_PKINIT_KP_KDC, str)
        self.assertIsInstance(Security.kSecOIDKeyUsage, str)
        self.assertIsInstance(Security.kSecOIDLocalityName, str)
        self.assertIsInstance(Security.kSecOIDMS_NTPrincipalName, str)
        self.assertIsInstance(Security.kSecOIDMicrosoftSGC, str)
        self.assertIsInstance(Security.kSecOIDNameConstraints, str)
        self.assertIsInstance(Security.kSecOIDNetscapeCertSequence, str)
        self.assertIsInstance(Security.kSecOIDNetscapeCertType, str)
        self.assertIsInstance(Security.kSecOIDNetscapeSGC, str)
        self.assertIsInstance(Security.kSecOIDOCSPSigning, str)
        self.assertIsInstance(Security.kSecOIDOrganizationName, str)
        self.assertIsInstance(Security.kSecOIDOrganizationalUnitName, str)
        self.assertIsInstance(Security.kSecOIDPolicyConstraints, str)
        self.assertIsInstance(Security.kSecOIDPolicyMappings, str)
        self.assertIsInstance(Security.kSecOIDPrivateKeyUsagePeriod, str)
        self.assertIsInstance(Security.kSecOIDQC_Statements, str)
        self.assertIsInstance(Security.kSecOIDSerialNumber, str)
        self.assertIsInstance(Security.kSecOIDServerAuth, str)
        self.assertIsInstance(Security.kSecOIDStateProvinceName, str)
        self.assertIsInstance(Security.kSecOIDStreetAddress, str)
        self.assertIsInstance(Security.kSecOIDSubjectAltName, str)
        self.assertIsInstance(Security.kSecOIDSubjectDirectoryAttributes, str)
        self.assertIsInstance(Security.kSecOIDSubjectEmailAddress, str)
        self.assertIsInstance(Security.kSecOIDSubjectInfoAccess, str)
        self.assertIsInstance(Security.kSecOIDSubjectKeyIdentifier, str)
        self.assertIsInstance(Security.kSecOIDSubjectPicture, str)
        self.assertIsInstance(Security.kSecOIDSubjectSignatureBitmap, str)
        self.assertIsInstance(Security.kSecOIDSurname, str)
        self.assertIsInstance(Security.kSecOIDTimeStamping, str)
        self.assertIsInstance(Security.kSecOIDTitle, str)
        self.assertIsInstance(Security.kSecOIDUseExemptions, str)
        self.assertIsInstance(Security.kSecOIDX509V1CertificateIssuerUniqueId, str)
        self.assertIsInstance(Security.kSecOIDX509V1CertificateSubjectUniqueId, str)
        self.assertIsInstance(Security.kSecOIDX509V1IssuerName, str)
        self.assertIsInstance(Security.kSecOIDX509V1IssuerNameCStruct, str)
        self.assertIsInstance(Security.kSecOIDX509V1IssuerNameLDAP, str)
        self.assertIsInstance(Security.kSecOIDX509V1IssuerNameStd, str)
        self.assertIsInstance(Security.kSecOIDX509V1SerialNumber, str)
        self.assertIsInstance(Security.kSecOIDX509V1Signature, str)
        self.assertIsInstance(Security.kSecOIDX509V1SignatureAlgorithm, str)
        self.assertIsInstance(Security.kSecOIDX509V1SignatureAlgorithmParameters, str)
        self.assertIsInstance(Security.kSecOIDX509V1SignatureAlgorithmTBS, str)
        self.assertIsInstance(Security.kSecOIDX509V1SignatureCStruct, str)
        self.assertIsInstance(Security.kSecOIDX509V1SignatureStruct, str)
        self.assertIsInstance(Security.kSecOIDX509V1SubjectName, str)
        self.assertIsInstance(Security.kSecOIDX509V1SubjectNameCStruct, str)
        self.assertIsInstance(Security.kSecOIDX509V1SubjectNameLDAP, str)
        self.assertIsInstance(Security.kSecOIDX509V1SubjectNameStd, str)
        self.assertIsInstance(Security.kSecOIDX509V1SubjectPublicKey, str)
        self.assertIsInstance(Security.kSecOIDX509V1SubjectPublicKeyAlgorithm, str)
        self.assertIsInstance(
            Security.kSecOIDX509V1SubjectPublicKeyAlgorithmParameters, str
        )
        self.assertIsInstance(Security.kSecOIDX509V1SubjectPublicKeyCStruct, str)
        self.assertIsInstance(Security.kSecOIDX509V1ValidityNotAfter, str)
        self.assertIsInstance(Security.kSecOIDX509V1ValidityNotBefore, str)
        self.assertIsInstance(Security.kSecOIDX509V1Version, str)
        self.assertIsInstance(Security.kSecOIDX509V3Certificate, str, str)
        self.assertIsInstance(Security.kSecOIDX509V3CertificateCStruct, str)
        self.assertIsInstance(Security.kSecOIDX509V3CertificateExtensionCStruct, str)
        self.assertIsInstance(Security.kSecOIDX509V3CertificateExtensionCritical, str)
        self.assertIsInstance(Security.kSecOIDX509V3CertificateExtensionId, str)
        self.assertIsInstance(Security.kSecOIDX509V3CertificateExtensionStruct, str)
        self.assertIsInstance(Security.kSecOIDX509V3CertificateExtensionType, str)
        self.assertIsInstance(Security.kSecOIDX509V3CertificateExtensionValue, str)
        self.assertIsInstance(Security.kSecOIDX509V3CertificateExtensionsCStruct, str)
        self.assertIsInstance(Security.kSecOIDX509V3CertificateExtensionsStruct, str)
        self.assertIsInstance(Security.kSecOIDX509V3CertificateNumberOfExtensions, str)
        self.assertIsInstance(Security.kSecOIDX509V3SignedCertificate, str)
        self.assertIsInstance(Security.kSecOIDX509V3SignedCertificateCStruct, str)

    @expectedFailure
    @min_os_level("10.7")
    def test_constants_missing(self):
        self.assertIsInstance(Security.kSecOIDAPPLE_EXTENSION_INTERMEDIATE_MARKER, str)
        self.assertIsInstance(Security.kSecOIDAPPLE_EXTENSION_WWDR_INTERMEDIATE, str)
        self.assertIsInstance(Security.kSecOIDAPPLE_EXTENSION_ITMS_INTERMEDIATE, str)
        self.assertIsInstance(Security.kSecOIDAPPLE_EXTENSION_AAI_INTERMEDIATE, str)
        self.assertIsInstance(Security.kSecOIDAPPLE_EXTENSION_APPLEID_INTERMEDIATE, str)

    @min_os_level("10.8")
    def test_constants_10_8(self):
        self.assertIsInstance(Security.kSecOIDSRVName, str)
