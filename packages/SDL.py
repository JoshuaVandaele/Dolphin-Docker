from packages.GenericOptionalPackage import GenericOptionalPackage


class SDL(GenericOptionalPackage):
    NAME = "SDL"

    @staticmethod
    def disable_configure_flag() -> str:
        return "-DENABLE_SDL=OFF"

    @staticmethod
    def debian() -> str:
        return "libsdl3-dev"

    @staticmethod
    def ubuntu() -> str:
        return "libsdl3-dev"

    @staticmethod
    def fedora() -> str:
        return "SDL3-devel"

    @staticmethod
    def arch() -> str:
        return "sdl3"

    @staticmethod
    def alpine() -> str:
        return "sdl3-dev"
