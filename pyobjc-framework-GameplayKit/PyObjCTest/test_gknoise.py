from PyObjCTools.TestSupport import TestCase

import GameplayKit

from objc import simd


class TestGKNoise(TestCase):
    def testMethods(self):
        self.assertArgIsBOOL(
            GameplayKit.GKNoise.remapValuesToTerracesWithPeaks_terracesInverted_, 1
        )

        self.assertArgHasType(
            GameplayKit.GKNoise.valueAtPosition_, 0, simd.vector_float2.__typestr__
        )
        self.assertArgHasType(
            GameplayKit.GKNoise.moveBy_, 0, simd.vector_double3.__typestr__
        )
        self.assertArgHasType(
            GameplayKit.GKNoise.scaleBy_, 0, simd.vector_double3.__typestr__
        )
        self.assertArgHasType(
            GameplayKit.GKNoise.rotateBy_, 0, simd.vector_double3.__typestr__
        )
