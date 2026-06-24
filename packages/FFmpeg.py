from packages.GenericOptionalPackage import GenericOptionalPackage


class FFmpeg(GenericOptionalPackage):
    NAME = "FFmpeg"

    @staticmethod
    def disable_configure_flag() -> str:
        return "-DENCODE_FRAMEDUMPS=OFF"

    @staticmethod
    def debian() -> str:
        return "libavcodec-dev libavformat-dev libavutil-dev libswresample-dev libswscale-dev"

    @staticmethod
    def ubuntu() -> str:
        return "libavcodec-dev libavformat-dev libavutil-dev libswresample-dev libswscale-dev"

    @staticmethod
    def fedora() -> str:
        return "libavcodec-free-devel libavformat-free-devel libavutil-free-devel libswresample-free-devel libswscale-free-devel"

    @staticmethod
    def arch() -> str:
        return "ffmpeg"

    @staticmethod
    def alpine() -> str:
        return "ffmpeg-dev"
