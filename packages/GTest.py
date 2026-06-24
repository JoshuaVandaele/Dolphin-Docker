from packages.GenericOptionalPackage import GenericOptionalPackage


class GTest(GenericOptionalPackage):
    NAME = "GoogleTest"

    @staticmethod
    def disable_configure_flag() -> str:
        return "-DENABLE_TESTS=OFF"

    @staticmethod
    def debian() -> str:
        return "libgtest-dev"

    @staticmethod
    def ubuntu() -> str:
        return "libgtest-dev"

    @staticmethod
    def fedora() -> str:
        return "gtest-devel"

    @staticmethod
    def arch() -> str:
        return "gtest"

    @staticmethod
    def alpine() -> str:
        return "gtest-dev"
