from packages.GenericPackage import GenericPackage


class CMake(GenericPackage):
    NAME = "CMake"

    @staticmethod
    def debian() -> str:
        return "cmake"

    @staticmethod
    def ubuntu() -> str:
        return "cmake"

    @staticmethod
    def fedora() -> str:
        return "cmake"

    @staticmethod
    def arch() -> str:
        return "cmake"

    @staticmethod
    def alpine() -> str:
        return "cmake"
