from packages.GenericOptionalPackage import GenericOptionalPackage


class LZO(GenericOptionalPackage):
    NAME = "LZO"

    @staticmethod
    def disable_configure_flag() -> str:
        return "-DUSE_SYSTEM_LZO=OFF"

    @staticmethod
    def debian() -> str:
        return "liblzo2-dev"

    @staticmethod
    def ubuntu() -> str:
        return "liblzo2-dev"

    @staticmethod
    def fedora() -> str:
        return "lzo-devel"

    @staticmethod
    def arch() -> str:
        return "lzo"

    @staticmethod
    def alpine() -> str:
        return "lzo-dev"
