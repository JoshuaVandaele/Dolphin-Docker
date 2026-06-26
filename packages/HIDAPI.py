from packages.GenericOptionalPackage import GenericOptionalPackage


class HIDAPI(GenericOptionalPackage):
    NAME = "HIDAPI"

    @staticmethod
    def disable_configure_flag() -> str:
        return "-DUSE_SYSTEM_HIDAPI=OFF"

    @staticmethod
    def debian() -> str:
        return "libhidapi-dev"

    @staticmethod
    def ubuntu() -> str:
        return "libhidapi-dev"

    @staticmethod
    def fedora() -> str:
        return "hidapi-devel"

    @staticmethod
    def arch() -> str:
        return "hidapi"

    @staticmethod
    def alpine() -> str:
        return "hidapi-dev"

    @staticmethod
    def gentoo() -> str:
        return "dev-libs/hidapi"
