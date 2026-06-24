from distros.GenericDistro import GenericDistro
from package_managers.APK import APK


class Alpine(GenericDistro):
    NAME = "alpine"
    IMAGE = "alpine:latest"
    PACKAGE_MANAGER = APK

    def __init__(self, base, required, optional, gcc, clang, quirks):
        self.packages: dict[str, list[str]] = {
            "base": [p.alpine() for p in base],
            "required": [p.alpine() for p in required],
            "optional": [p.alpine() for p in optional],
            "gcc": [p.alpine() for p in gcc],
            "clang": [p.alpine() for p in clang],
            "quirks": [p.disable_configure_flag() for p in quirks],
        }
