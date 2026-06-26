from packages.GenericOptionalPackage import GenericOptionalPackage


class Zstd(GenericOptionalPackage):
    NAME = "Zstandard"

    @staticmethod
    def disable_configure_flag() -> str:
        return "-DUSE_SYSTEM_ZSTD=OFF"

    @staticmethod
    def debian() -> str:
        return "libzstd-dev"

    @staticmethod
    def ubuntu() -> str:
        return "libzstd-dev"

    @staticmethod
    def fedora() -> str:
        return "libzstd-devel"

    @staticmethod
    def arch() -> str:
        return "zstd"

    @staticmethod
    def alpine() -> str:
        return "zstd-dev"

    @staticmethod
    def gentoo() -> str:
        return "app-arch/zstd"
