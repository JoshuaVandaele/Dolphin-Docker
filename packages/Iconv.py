from packages.GenericOptionalPackage import GenericOptionalPackage


class Iconv(GenericOptionalPackage):
    NAME = "iconv"

    @staticmethod
    def disable_configure_flag() -> str:
        return "-DUSE_SYSTEM_ICONV=OFF"

    @staticmethod
    def debian() -> str:
        # Built-in
        return ""

    @staticmethod
    def ubuntu() -> str:
        # Built-in
        return ""

    @staticmethod
    def fedora() -> str:
        # Built-in
        return ""

    @staticmethod
    def arch() -> str:
        return "libiconv"

    @staticmethod
    def alpine() -> str:
        # Built-in
        return ""

    @staticmethod
    def gentoo() -> str:
        # Built-in
        return ""
