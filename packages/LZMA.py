from packages.GenericOptionalPackage import GenericOptionalPackage


class LZMA(GenericOptionalPackage):
    NAME = "libLZMA"

    @staticmethod
    def disable_configure_flag() -> str:
        return "-DUSE_SYSTEM_LIBLZMA=OFF"

    @staticmethod
    def debian() -> str:
        return "liblzma-dev"

    @staticmethod
    def ubuntu() -> str:
        return "liblzma-dev"

    @staticmethod
    def fedora() -> str:
        return "xz-devel"

    @staticmethod
    def arch() -> str:
        return "xz"

    @staticmethod
    def alpine() -> str:
        return "xz-dev"
