from packages.GenericOptionalPackage import GenericOptionalPackage


class MGBA(GenericOptionalPackage):
    NAME = "libmGBA"

    @staticmethod
    def disable_configure_flag() -> str:
        return "-DUSE_MGBA=OFF"

    @staticmethod
    def debian() -> str:
        return "libmgba-dev"

    @staticmethod
    def ubuntu() -> str:
        return "libmgba-dev"

    @staticmethod
    def fedora() -> str:
        raise NotImplementedError("Not in the repository.")

    @staticmethod
    def arch() -> str:
        return "libmgba"

    @staticmethod
    def alpine() -> str:
        return "libmgba-dev"
