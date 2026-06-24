from packages.GenericOptionalPackage import GenericOptionalPackage


class Fmt(GenericOptionalPackage):
    NAME = "{fmt}"

    @staticmethod
    def disable_configure_flag() -> str:
        return "-DUSE_SYSTEM_FMT=OFF"

    @staticmethod
    def debian() -> str:
        return "libfmt-dev"

    @staticmethod
    def ubuntu() -> str:
        return "libfmt-dev"

    @staticmethod
    def fedora() -> str:
        return "fmt-devel"

    @staticmethod
    def arch() -> str:
        return "fmt"

    @staticmethod
    def alpine() -> str:
        return "fmt-dev"
