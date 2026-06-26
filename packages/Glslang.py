from packages.GenericOptionalPackage import GenericOptionalPackage


class Glslang(GenericOptionalPackage):
    NAME = "glslang"

    @staticmethod
    def disable_configure_flag() -> str:
        return "-DUSE_SYSTEM_GLSLANG=OFF"

    @staticmethod
    def debian() -> str:
        return "glslang-tools glslang-dev"

    @staticmethod
    def ubuntu() -> str:
        return "glslang-tools glslang-dev"

    @staticmethod
    def fedora() -> str:
        return "glslang-devel"

    @staticmethod
    def arch() -> str:
        return "glslang"

    @staticmethod
    def alpine() -> str:
        return "glslang-dev spirv-tools-dev"

    @staticmethod
    def gentoo() -> str:
        return "dev-util/glslang"
