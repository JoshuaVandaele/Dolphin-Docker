from packages.GenericPackage import GenericPackage


class LibCPlusPlus(GenericPackage):
    NAME = "libc++"

    @staticmethod
    def debian() -> str:
        return "libc++-dev"

    @staticmethod
    def ubuntu() -> str:
        return "libc++-dev"

    @staticmethod
    def fedora() -> str:
        return "libcxx-devel"

    @staticmethod
    def arch() -> str:
        return "libc++"

    @staticmethod
    def alpine() -> str:
        return "libc++-dev"
