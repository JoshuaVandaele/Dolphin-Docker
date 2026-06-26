from packages.GenericOptionalPackage import GenericOptionalPackage


class XxHash(GenericOptionalPackage):
    NAME = "xxHash"

    @staticmethod
    def disable_configure_flag() -> str:
        return "-DUSE_SYSTEM_XXHASH=OFF"

    @staticmethod
    def debian() -> str:
        return "libxxhash-dev"

    @staticmethod
    def ubuntu() -> str:
        return "libxxhash-dev"

    @staticmethod
    def fedora() -> str:
        return "xxhash-devel"

    @staticmethod
    def arch() -> str:
        return "xxhash"

    @staticmethod
    def alpine() -> str:
        return "xxhash-dev"

    @staticmethod
    def gentoo() -> str:
        return "dev-libs/xxhash"
