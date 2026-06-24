from packages.GenericOptionalPackage import GenericOptionalPackage


class LibCurl(GenericOptionalPackage):
    NAME = "libcurl"

    @staticmethod
    def disable_configure_flag() -> str:
        return "-DUSE_SYSTEM_CURL=OFF"

    @staticmethod
    def debian() -> str:
        return "libcurl4-openssl-dev"

    @staticmethod
    def ubuntu() -> str:
        return "libcurl4-openssl-dev"

    @staticmethod
    def fedora() -> str:
        return "libcurl-devel"

    @staticmethod
    def arch() -> str:
        return "curl"

    @staticmethod
    def alpine() -> str:
        return "curl-dev"
