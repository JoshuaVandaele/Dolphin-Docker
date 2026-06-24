from packages.GenericPackage import GenericPackage


class GPlusPlus(GenericPackage):
    NAME = "G++"

    @staticmethod
    def debian() -> str:
        return "g++"

    @staticmethod
    def ubuntu() -> str:
        return "g++"

    @staticmethod
    def fedora() -> str:
        return "gcc-c++"

    @staticmethod
    def arch() -> str:
        return "gcc"

    @staticmethod
    def alpine() -> str:
        return "g++"
