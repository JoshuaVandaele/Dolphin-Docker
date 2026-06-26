from packages.GenericOptionalPackage import GenericOptionalPackage


class PkgConfig(GenericOptionalPackage):
    NAME = "PkgConfig"

    @staticmethod
    def disable_configure_flag() -> str:
        # Not used if not found, I think?
        return ""

    @staticmethod
    def debian() -> str:
        return "pkg-config"

    @staticmethod
    def ubuntu() -> str:
        return "pkg-config"

    @staticmethod
    def fedora() -> str:
        return "pkgconf-pkg-config"

    @staticmethod
    def arch() -> str:
        return "pkgconf"

    @staticmethod
    def alpine() -> str:
        return "pkgconf"

    @staticmethod
    def gentoo() -> str:
        return "virtual/pkgconfig"
