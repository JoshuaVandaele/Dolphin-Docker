from distros.GenericDistro import GenericDistro
from package_managers.APT import APT


class Debian(GenericDistro):
    NAME = "debian"
    IMAGE = "debian:latest"
    PACKAGE_MANAGER = APT

    def __init__(self, base, required, optional, gcc, clang, quirks):
        self.packages: dict[str, list[str]] = {
            "base": [p.debian() for p in base],
            "required": [p.debian() for p in required],
            "optional": [p.debian() for p in optional],
            "gcc": [p.debian() for p in gcc],
            "clang": [p.debian() for p in clang],
            "quirks": [p.disable_configure_flag() for p in quirks],
        }
