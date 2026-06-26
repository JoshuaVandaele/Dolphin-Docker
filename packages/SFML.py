from packages.GenericOptionalPackage import GenericOptionalPackage


class SFML(GenericOptionalPackage):
    NAME = "SFML"

    @staticmethod
    def disable_configure_flag() -> str:
        return "-DUSE_SYSTEM_SFML=OFF"

    @staticmethod
    def debian() -> str:
        return "libsfml-dev"

    @staticmethod
    def ubuntu() -> str:
        return "libsfml-dev"

    @staticmethod
    def fedora() -> str:
        return "SFML-devel"

    @staticmethod
    def arch() -> str:
        return "sfml"

    @staticmethod
    def alpine() -> str:
        return "sfml-dev"

    @staticmethod
    def gentoo() -> str:
        return "media-libs/libsfml"
