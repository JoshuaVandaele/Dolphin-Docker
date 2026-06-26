from packages.GenericOptionalPackage import GenericOptionalPackage


class LibUSB(GenericOptionalPackage):
    NAME = "libusb"

    @staticmethod
    def disable_configure_flag() -> str:
        return "-DUSE_SYSTEM_LIBUSB=OFF"

    @staticmethod
    def debian() -> str:
        return "libusb-1.0-0-dev"

    @staticmethod
    def ubuntu() -> str:
        return "libusb-1.0-0-dev"

    @staticmethod
    def fedora() -> str:
        return "libusb1-devel"

    @staticmethod
    def arch() -> str:
        return "libusb"

    @staticmethod
    def alpine() -> str:
        return "libusb-dev"

    @staticmethod
    def gentoo() -> str:
        return "virtual/libusb"
