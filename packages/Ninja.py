from packages.GenericPackage import GenericPackage


class Ninja(GenericPackage):
    NAME = "Ninja"

    @staticmethod
    def debian() -> str:
        return "ninja-build"

    @staticmethod
    def ubuntu() -> str:
        return "ninja-build"

    @staticmethod
    def fedora() -> str:
        return "ninja-build"

    @staticmethod
    def arch() -> str:
        return "ninja"

    @staticmethod
    def alpine() -> str:
        return "ninja"
