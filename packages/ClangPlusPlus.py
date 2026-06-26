from packages.GenericPackage import GenericPackage


class ClangPlusPlus(GenericPackage):
    NAME = "Clang++"

    @staticmethod
    def debian() -> str:
        return "clang"

    @staticmethod
    def ubuntu() -> str:
        return "clang"

    @staticmethod
    def fedora() -> str:
        return "clang"

    @staticmethod
    def arch() -> str:
        return "clang"

    @staticmethod
    def alpine() -> str:
        return "clang"

    @staticmethod
    def gentoo() -> str:
        return "llvm-core/clang"
