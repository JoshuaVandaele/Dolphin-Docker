from packages.GenericOptionalPackage import GenericOptionalPackage


class OpenGL(GenericOptionalPackage):
    NAME = "OpenGL"

    @staticmethod
    def disable_configure_flag() -> str:
        # Not used if not found
        return ""

    @staticmethod
    def debian() -> str:
        return "libgl1-mesa-dev"

    @staticmethod
    def ubuntu() -> str:
        return "libgl1-mesa-dev"

    @staticmethod
    def fedora() -> str:
        return "mesa-libGL-devel"

    @staticmethod
    def arch() -> str:
        return "libglvnd"

    @staticmethod
    def alpine() -> str:
        return "glfw-dev"

    @staticmethod
    def gentoo() -> str:
        return "virtual/opengl"
