from packages.GenericOptionalPackage import GenericOptionalPackage


class PulseAudio(GenericOptionalPackage):
    NAME = "PulseAudio"

    @staticmethod
    def disable_configure_flag() -> str:
        return "-DENABLE_PULSEAUDIO=OFF"

    @staticmethod
    def debian() -> str:
        return "libpulse-dev"

    @staticmethod
    def ubuntu() -> str:
        return "libpulse-dev"

    @staticmethod
    def fedora() -> str:
        return "pulseaudio-libs-devel"

    @staticmethod
    def arch() -> str:
        return "libpulse"

    @staticmethod
    def alpine() -> str:
        return "pulseaudio-dev"

    @staticmethod
    def gentoo() -> str:
        return "media-libs/libpulse"
