from abc import ABC

from package_managers.GenericPackageManager import GenericPackageManager
from packages.GenericOptionalPackage import GenericOptionalPackage
from packages.GenericPackage import GenericPackage


class GenericDistro(ABC):
    NAME: str
    IMAGE: str
    PACKAGE_MANAGER: type[GenericPackageManager]

    def __init__(
        self,
        base: list[type[GenericPackage]],
        required: list[type[GenericPackage]],
        optional: list[type[GenericPackage]],
        gcc: list[type[GenericPackage]],
        clang: list[type[GenericPackage]],
        quirks: list[type[GenericOptionalPackage]],
    ):
        self.packages: dict[str, list[str]]
