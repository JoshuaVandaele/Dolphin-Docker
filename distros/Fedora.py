from distros.GenericDistro import GenericDistro
from package_managers.DNF import DNF


class Fedora(GenericDistro):
    NAME = "fedora"
    IMAGE = "fedora:latest"
    PACKAGE_MANAGER = DNF

    def __init__(self, base, required, optional, gcc, clang, quirks):
        self.packages: dict[str, list[str]] = {
            "base": [p.fedora() for p in base],
            "required": [p.fedora() for p in required],
            "optional": [p.fedora() for p in optional],
            "gcc": [p.fedora() for p in gcc],
            "clang": [p.fedora() for p in clang],
            "quirks": [p.disable_configure_flag() for p in quirks],
        }
