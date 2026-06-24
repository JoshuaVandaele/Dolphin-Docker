from packages.GenericPackage import GenericPackage


class LibSTDCPlusPlus(GenericPackage):
    NAME = "libstdc++"

    @staticmethod
    def debian() -> str:
        return "g++"  # libstdc++-dev fails because it's a "virtual package" or whatever nonsense

    @staticmethod
    def ubuntu() -> str:
        return "libstdc++-dev"

    @staticmethod
    def fedora() -> str:
        return "libstdc++"

    @staticmethod
    def arch() -> str:
        return "libstdc++"

    @staticmethod
    def alpine() -> str:
        return "libstdc++-dev"
