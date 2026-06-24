from packages.GenericOptionalPackage import GenericOptionalPackage


class Zlib(GenericOptionalPackage):
    NAME = "zlib"

    @staticmethod
    def disable_configure_flag() -> str:
        return "-DUSE_SYSTEM_ZLIB=OFF"

    @staticmethod
    def debian() -> str:
        return "zlib1g-dev"

    @staticmethod
    def ubuntu() -> str:
        return "zlib1g-dev"

    @staticmethod
    def fedora() -> str:
        return "zlib-devel"

    @staticmethod
    def arch() -> str:
        return "zlib-ng"

    @staticmethod
    def alpine() -> str:
        return "zlib-dev"
