from packages.GenericOptionalPackage import GenericOptionalPackage


class Systemd(GenericOptionalPackage):
    NAME = "systemd"

    @staticmethod
    def disable_configure_flag() -> str:
        # Not used if not found
        return ""

    @staticmethod
    def debian() -> str:
        return "libsystemd-dev"

    @staticmethod
    def ubuntu() -> str:
        return "libsystemd-dev"

    @staticmethod
    def fedora() -> str:
        return "systemd-devel"

    @staticmethod
    def arch() -> str:
        return "systemd-libs"

    @staticmethod
    def alpine() -> str:
        # Alpine doesn't use sytemd
        raise NotImplementedError("Not in the repository.")

    @staticmethod
    def gentoo() -> str:
        return "sys-apps/systemd-utils"
