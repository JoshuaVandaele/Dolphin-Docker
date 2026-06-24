from packages.GenericOptionalPackage import GenericOptionalPackage


class Pugixml(GenericOptionalPackage):
    NAME = "pugixml"

    @staticmethod
    def disable_configure_flag() -> str:
        return "-DUSE_SYSTEM_PUGIXML=OFF"

    @staticmethod
    def debian() -> str:
        return "libpugixml-dev"

    @staticmethod
    def ubuntu() -> str:
        return "libpugixml-dev"

    @staticmethod
    def fedora() -> str:
        return "pugixml-devel"

    @staticmethod
    def arch() -> str:
        return "pugixml"

    @staticmethod
    def alpine() -> str:
        return "pugixml-dev"
