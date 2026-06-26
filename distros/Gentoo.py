from distros.GenericDistro import GenericDistro
from package_managers.Portage import Portage


class Gentoo(GenericDistro):
    NAME = "gentoo"
    IMAGE = "gentoo/stage3:latest"
    PACKAGE_MANAGER = Portage

    def __init__(self, base, required, optional, gcc, clang, quirks):
        self.packages: dict[str, list[str]] = {
            "base": [p.gentoo() for p in base],
            "required": [p.gentoo() for p in required],
            "optional": [p.gentoo() for p in optional],
            "gcc": [p.gentoo() for p in gcc],
            "clang": [p.gentoo() for p in clang],
            "quirks": [p.disable_configure_flag() for p in quirks],
        }
