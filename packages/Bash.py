from packages.GenericPackage import GenericPackage


class Bash(GenericPackage):
    NAME = "Bash"

    @staticmethod
    def debian() -> str:
        return "bash"

    @staticmethod
    def ubuntu() -> str:
        return "bash"

    @staticmethod
    def fedora() -> str:
        return "bash"

    @staticmethod
    def arch() -> str:
        return "bash"

    @staticmethod
    def alpine() -> str:
        return "bash"

    @staticmethod
    def gentoo() -> str:
        return "app-shells/bash"
