from packages.GenericOptionalPackage import GenericOptionalPackage


class Qt6(GenericOptionalPackage):
    NAME = "Qt 6"

    @staticmethod
    def disable_configure_flag() -> str:
        return "-DENABLE_HEADLESS=ON"

    @staticmethod
    def debian() -> str:
        return "qt6-base-dev qt6-base-private-dev qt6-svg-dev"

    @staticmethod
    def ubuntu() -> str:
        return "qt6-base-dev qt6-base-private-dev qt6-svg-dev"

    @staticmethod
    def fedora() -> str:
        return "qt6-qtbase-devel qt6-qtbase-private-devel qt6-qtsvg-devel"

    @staticmethod
    def arch() -> str:
        return "qt6-base qt6-svg"

    @staticmethod
    def alpine() -> str:
        return "qt6-qtbase-dev qt6-qtbase-private-dev qt6-qtsvg-dev"
