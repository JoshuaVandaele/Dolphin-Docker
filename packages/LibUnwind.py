from packages.GenericPackage import GenericPackage


class LibUnwind(GenericPackage):
    NAME = "libunwind"

    @staticmethod
    def debian() -> str:
        return ""  ## "libunwind-dev" Conflicts with libunwind-XX-dev pulled by libc++

    @staticmethod
    def ubuntu() -> str:
        return "libunwind-dev"

    @staticmethod
    def fedora() -> str:
        return "llvm-libunwind"

    @staticmethod
    def arch() -> str:
        return "libunwind"

    @staticmethod
    def alpine() -> str:
        return "llvm-libunwind-dev"
