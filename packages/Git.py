from packages.GenericPackage import GenericPackage


class Git(GenericPackage):
    NAME = "Git"

    @staticmethod
    def debian() -> str:
        return "git"

    @staticmethod
    def ubuntu() -> str:
        return "git"

    @staticmethod
    def fedora() -> str:
        return "git"

    @staticmethod
    def arch() -> str:
        return "git"

    @staticmethod
    def alpine() -> str:
        return "git"

    @staticmethod
    def gentoo() -> str:
        return "dev-vcs/git"
