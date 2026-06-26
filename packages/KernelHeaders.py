from packages.GenericPackage import GenericPackage


class KernelHeaders(GenericPackage):
    NAME = "Linux headers"

    @staticmethod
    def debian() -> str:
        return "linux-libc-dev"

    @staticmethod
    def ubuntu() -> str:
        return "linux-libc-dev"

    @staticmethod
    def fedora() -> str:
        return "kernel-headers"

    @staticmethod
    def arch() -> str:
        return "linux-headers"

    @staticmethod
    def alpine() -> str:
        return "linux-headers"

    @staticmethod
    def gentoo() -> str:
        return "sys-kernel/linux-headers"
