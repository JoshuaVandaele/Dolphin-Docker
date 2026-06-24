from distros.GenericDistro import GenericDistro
from package_managers.Pacman import Pacman


class Arch(GenericDistro):
    NAME = "arch"
    IMAGE = "archlinux:latest"
    PACKAGE_MANAGER = Pacman

    def __init__(self, base, required, optional, gcc, clang, quirks):
        self.packages: dict[str, list[str]] = {
            "base": [p.arch() for p in base],
            "required": [p.arch() for p in required],
            "optional": [p.arch() for p in optional],
            "gcc": [p.arch() for p in gcc],
            "clang": [p.arch() for p in clang],
            "quirks": [p.disable_configure_flag() for p in quirks],
        }
