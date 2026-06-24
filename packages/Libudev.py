from packages.GenericOptionalPackage import GenericOptionalPackage


class Libudev(GenericOptionalPackage):
    NAME = "libudev"

    @staticmethod
    def disable_configure_flag() -> str:
        return "-DENABLE_HWDB=OFF -DENABLE_EVDEV=OFF"

    @staticmethod
    def debian() -> str:
        return "libudev-dev"

    @staticmethod
    def ubuntu() -> str:
        return "libudev-dev"

    @staticmethod
    def fedora() -> str:
        return "systemd-devel"

    @staticmethod
    def arch() -> str:
        return "systemd-libs"

    @staticmethod
    def alpine() -> str:
        return "eudev-dev"
