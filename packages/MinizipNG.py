from packages.GenericOptionalPackage import GenericOptionalPackage


class MinizipNG(GenericOptionalPackage):
    NAME = "minizip-ng"

    @staticmethod
    def disable_configure_flag() -> str:
        return "-DUSE_SYSTEM_MINIZIP-NG=OFF"

    @staticmethod
    def debian() -> str:
        return "libminizip-ng-dev"

    @staticmethod
    def ubuntu() -> str:
        return "libminizip-ng-dev"

    @staticmethod
    def fedora() -> str:
        return "minizip-ng-devel"

    @staticmethod
    def arch() -> str:
        return "minizip-ng"

    @staticmethod
    def alpine() -> str:
        return "minizip-ng-dev"
