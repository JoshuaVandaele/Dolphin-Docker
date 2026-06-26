from packages.GenericOptionalPackage import GenericOptionalPackage


class Miniupnpc(GenericOptionalPackage):
    NAME = "miniupnpc"

    @staticmethod
    def disable_configure_flag() -> str:
        return "-DUSE_UPNP=OFF"

    @staticmethod
    def debian() -> str:
        return "libminiupnpc-dev"

    @staticmethod
    def ubuntu() -> str:
        return "libminiupnpc-dev"

    @staticmethod
    def fedora() -> str:
        return "miniupnpc-devel"

    @staticmethod
    def arch() -> str:
        return "miniupnpc"

    @staticmethod
    def alpine() -> str:
        return "miniupnpc-dev"

    @staticmethod
    def gentoo() -> str:
        return "net-libs/miniupnpc"
