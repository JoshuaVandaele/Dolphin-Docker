from packages.GenericOptionalPackage import GenericOptionalPackage


class X11(GenericOptionalPackage):
    NAME = "X11"

    @staticmethod
    def disable_configure_flag() -> str:
        return "-DENABLE_X11=OFF"

    @staticmethod
    def debian() -> str:
        return "libx11-dev libxrandr-dev libxi-dev"

    @staticmethod
    def ubuntu() -> str:
        return "libx11-dev libxrandr-dev libxi-dev"

    @staticmethod
    def fedora() -> str:
        return "libX11-devel libXrandr-devel libXi-devel"

    @staticmethod
    def arch() -> str:
        return "libx11 libxrandr libxi"

    @staticmethod
    def alpine() -> str:
        return "libx11-dev libxrandr-dev libxi-dev"

    @staticmethod
    def gentoo() -> str:
        return "x11-libs/libX11 x11-libs/libXi x11-libs/libXrandr"
