from packages.GenericOptionalPackage import GenericOptionalPackage


class EGL(GenericOptionalPackage):
    NAME = "EGL"

    @staticmethod
    def disable_configure_flag() -> str:
        return "-DENABLE_EGL=OFF"

    @staticmethod
    def debian() -> str:
        return "libegl1-mesa-dev"

    @staticmethod
    def ubuntu() -> str:
        return "libegl1-mesa-dev"

    @staticmethod
    def fedora() -> str:
        return "mesa-libEGL-devel"

    @staticmethod
    def arch() -> str:
        return "libglvnd"

    @staticmethod
    def alpine() -> str:
        return "mesa-egl"
