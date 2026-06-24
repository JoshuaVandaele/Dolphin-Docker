from packages.GenericOptionalPackage import GenericOptionalPackage


class LZ4(GenericOptionalPackage):
    NAME = "LZ4"

    @staticmethod
    def disable_configure_flag() -> str:
        return "-DUSE_SYSTEM_LZ4=OFF"

    @staticmethod
    def debian() -> str:
        return "liblz4-dev"

    @staticmethod
    def ubuntu() -> str:
        return "liblz4-dev"

    @staticmethod
    def fedora() -> str:
        return "lz4-devel"

    @staticmethod
    def arch() -> str:
        return "lz4"

    @staticmethod
    def alpine() -> str:
        return "lz4-dev"
