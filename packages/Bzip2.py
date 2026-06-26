from packages.GenericOptionalPackage import GenericOptionalPackage


class Bzip2(GenericOptionalPackage):
    NAME = "bzip2"

    @staticmethod
    def disable_configure_flag() -> str:
        return "-DUSE_SYSTEM_BZIP2=OFF"

    @staticmethod
    def debian() -> str:
        return "libbz2-dev"

    @staticmethod
    def ubuntu() -> str:
        return "libbz2-dev"

    @staticmethod
    def fedora() -> str:
        return "bzip2-devel"

    @staticmethod
    def arch() -> str:
        return "bzip2"

    @staticmethod
    def alpine() -> str:
        return "bzip2-dev"

    @staticmethod
    def gentoo() -> str:
        return "app-arch/bzip2"
