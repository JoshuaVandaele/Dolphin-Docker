from packages.GenericPackage import GenericPackage


class Ld(GenericPackage):
    NAME = "ld"

    @staticmethod
    def debian() -> str:
        return "binutils"

    @staticmethod
    def ubuntu() -> str:
        return "binutils"

    @staticmethod
    def fedora() -> str:
        return "binutils"

    @staticmethod
    def arch() -> str:
        return "binutils"

    @staticmethod
    def alpine() -> str:
        return "binutils"
