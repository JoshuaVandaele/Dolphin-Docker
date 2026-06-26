from packages.GenericOptionalPackage import GenericOptionalPackage


class ALSA(GenericOptionalPackage):
    NAME = "ALSA"

    @staticmethod
    def disable_configure_flag() -> str:
        return "-DENABLE_ALSA=OFF"

    @staticmethod
    def debian() -> str:
        return "libasound2-dev"

    @staticmethod
    def ubuntu() -> str:
        return "libasound2-dev"

    @staticmethod
    def fedora() -> str:
        return "alsa-lib-devel"

    @staticmethod
    def arch() -> str:
        return "alsa-lib"

    @staticmethod
    def alpine() -> str:
        return "alsa-lib-dev"

    @staticmethod
    def gentoo() -> str:
        return "media-libs/alsa-lib"
