from packages.GenericOptionalPackage import GenericOptionalPackage


class MbedTLS(GenericOptionalPackage):
    NAME = "MbedTLS 2"

    @staticmethod
    def disable_configure_flag() -> str:
        return "-DUSE_SYSTEM_MBEDTLS=OFF"

    @staticmethod
    def debian() -> str:
        return "libmbedtls-dev"

    @staticmethod
    def ubuntu() -> str:
        return "libmbedtls-dev"

    @staticmethod
    def fedora() -> str:
        return "mbedtls-devel"

    @staticmethod
    def arch() -> str:
        return "mbedtls2"

    @staticmethod
    def alpine() -> str:
        return "mbedtls2-dev"
