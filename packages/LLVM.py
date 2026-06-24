from packages.GenericOptionalPackage import GenericOptionalPackage


class LLVM(GenericOptionalPackage):
    NAME = "LLVM"

    @staticmethod
    def disable_configure_flag() -> str:
        return "-DENABLE_LLVM=OFF"

    @staticmethod
    def debian() -> str:
        return "llvm-dev"

    @staticmethod
    def ubuntu() -> str:
        return "llvm-dev"

    @staticmethod
    def fedora() -> str:
        return "llvm-devel"

    @staticmethod
    def arch() -> str:
        return "llvm"

    @staticmethod
    def alpine() -> str:
        return "llvm-dev"
