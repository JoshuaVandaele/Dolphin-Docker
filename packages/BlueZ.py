from packages.GenericOptionalPackage import GenericOptionalPackage


class BlueZ(GenericOptionalPackage):
    NAME = "BlueZ"

    @staticmethod
    def disable_configure_flag() -> str:
        return "-DENABLE_BLUEZ=OFF"

    @staticmethod
    def debian() -> str:
        return "libbluetooth-dev"

    @staticmethod
    def ubuntu() -> str:
        return "libbluetooth-dev"

    @staticmethod
    def fedora() -> str:
        return "bluez-libs-devel"

    @staticmethod
    def arch() -> str:
        return "bluez-libs"

    @staticmethod
    def alpine() -> str:
        return "bluez-dev"

    @staticmethod
    def gentoo() -> str:
        return "net-wireless/bluez"
