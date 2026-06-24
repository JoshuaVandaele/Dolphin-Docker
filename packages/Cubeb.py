from packages.GenericOptionalPackage import GenericOptionalPackage


class Cubeb(GenericOptionalPackage):
    NAME = "libcubeb"

    @staticmethod
    def disable_configure_flag() -> str:
        return "-DENABLE_CUBEB=OFF"

    @staticmethod
    def debian() -> str:
        return "libcubeb-dev"

    @staticmethod
    def ubuntu() -> str:
        return "libcubeb-dev"

    @staticmethod
    def fedora() -> str:
        return "cubeb-devel"

    @staticmethod
    def arch() -> str:
        raise NotImplementedError("Not in the repository.")

    @staticmethod
    def alpine() -> str:
        raise NotImplementedError("Not in the repository.")
