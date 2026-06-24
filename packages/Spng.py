from packages.GenericOptionalPackage import GenericOptionalPackage


class Spng(GenericOptionalPackage):
    NAME = "spng"

    @staticmethod
    def disable_configure_flag() -> str:
        return "-DUSE_SYSTEM_SPNG=OFF"

    @staticmethod
    def debian() -> str:
        return "libspng-dev"

    @staticmethod
    def ubuntu() -> str:
        return "libspng-dev"

    @staticmethod
    def fedora() -> str:
        return "libspng-devel"

    @staticmethod
    def arch() -> str:
        return "libspng"

    @staticmethod
    def alpine() -> str:
        return "libspng-dev"
