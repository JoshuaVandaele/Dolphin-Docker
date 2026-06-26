from packages.GenericPackage import GenericPackage


class LLVMArchiver(GenericPackage):
    NAME = "LLVM archiver"

    @staticmethod
    def debian() -> str:
        return "llvm"

    @staticmethod
    def ubuntu() -> str:
        return "llvm"

    @staticmethod
    def fedora() -> str:
        return "llvm"

    @staticmethod
    def arch() -> str:
        return "llvm"

    @staticmethod
    def alpine() -> str:
        return "llvm"

    @staticmethod
    def gentoo() -> str:
        return "llvm-core/llvm"
