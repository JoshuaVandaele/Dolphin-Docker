from packages.GenericPackage import GenericPackage


class CompilerRT(GenericPackage):
    NAME = "compiler-rt"

    @staticmethod
    def debian() -> str:
        return "libclang-rt-dev"

    @staticmethod
    def ubuntu() -> str:
        return "libclang-rt-dev"

    @staticmethod
    def fedora() -> str:
        return "compiler-rt"

    @staticmethod
    def arch() -> str:
        return "compiler-rt"

    @staticmethod
    def alpine() -> str:
        return "compiler-rt"
