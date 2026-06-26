from packages.GenericPackage import GenericPackage


class Ccache(GenericPackage):
    NAME = "Ccache"

    @staticmethod
    def debian() -> str:
        return "ccache"

    @staticmethod
    def ubuntu() -> str:
        return "ccache"

    @staticmethod
    def fedora() -> str:
        return "ccache"

    @staticmethod
    def arch() -> str:
        return "ccache"

    @staticmethod
    def alpine() -> str:
        return "ccache"

    @staticmethod
    def gentoo() -> str:
        return "dev-util/ccache"
