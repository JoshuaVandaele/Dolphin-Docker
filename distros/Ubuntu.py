from distros.GenericDistro import GenericDistro
from package_managers.APT import APT


class Ubuntu(GenericDistro):
    NAME = "ubuntu"
    IMAGE = "ubuntu:latest"
    PACKAGE_MANAGER = APT

    def __init__(self, base, required, optional, gcc, clang, quirks):
        self.packages: dict[str, list[str]] = {
            "base": [p.ubuntu() for p in base],
            "required": [p.ubuntu() for p in required],
            "optional": [p.ubuntu() for p in optional],
            "gcc": [p.ubuntu() for p in gcc],
            "clang": [p.ubuntu() for p in clang],
            "quirks": [p.disable_configure_flag() for p in quirks],
        }
