from packages.GenericOptionalPackage import GenericOptionalPackage


class ENet(GenericOptionalPackage):
    NAME = "ENet"

    @staticmethod
    def disable_configure_flag() -> str:
        return "-DUSE_SYSTEM_ENET=OFF"

    @staticmethod
    def debian() -> str:
        return "libenet-dev"

    @staticmethod
    def ubuntu() -> str:
        return "libenet-dev"

    @staticmethod
    def fedora() -> str:
        return "enet-devel"

    @staticmethod
    def arch() -> str:
        return "enet"

    @staticmethod
    def alpine() -> str:
        return "enet-dev"
