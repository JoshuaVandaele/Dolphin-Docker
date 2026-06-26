from packages.GenericOptionalPackage import GenericOptionalPackage


class Gettext(GenericOptionalPackage):
    NAME = "gettext"

    @staticmethod
    def disable_configure_flag() -> str:
        # Not used if not found
        return ""

    @staticmethod
    def debian() -> str:
        return "gettext"

    @staticmethod
    def ubuntu() -> str:
        return "gettext"

    @staticmethod
    def fedora() -> str:
        return "gettext"

    @staticmethod
    def arch() -> str:
        return "gettext"

    @staticmethod
    def alpine() -> str:
        return "gettext"

    @staticmethod
    def gentoo() -> str:
        return "sys-devel/gettext"
