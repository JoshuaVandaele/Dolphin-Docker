from packages.GenericPackage import GenericPackage


class LLD(GenericPackage):
    NAME = "LLD"

    @staticmethod
    def debian() -> str:
        return "lld"

    @staticmethod
    def ubuntu() -> str:
        return "lld"

    @staticmethod
    def fedora() -> str:
        return "lld"

    @staticmethod
    def arch() -> str:
        return "lld"

    @staticmethod
    def alpine() -> str:
        return "lld gcc"  # gcc is required for linking for some confusing reason

    @staticmethod
    def gentoo() -> str:
        return "llvm-core/lld"
