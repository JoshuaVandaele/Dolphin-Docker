from packages.GenericOptionalPackage import GenericOptionalPackage


class Libevdev(GenericOptionalPackage):
    NAME = "libevdev"

    @staticmethod
    def disable_configure_flag() -> str:
        return "-DENABLE_EVDEV=OFF"

    @staticmethod
    def debian() -> str:
        return "libevdev-dev"

    @staticmethod
    def ubuntu() -> str:
        return "libevdev-dev"

    @staticmethod
    def fedora() -> str:
        return "libevdev-devel"

    @staticmethod
    def arch() -> str:
        return "libevdev"

    @staticmethod
    def alpine() -> str:
        return "libevdev-dev"
