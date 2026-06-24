from abc import ABC, abstractmethod

from packages.GenericPackage import GenericPackage


class GenericOptionalPackage(GenericPackage, ABC):
    @staticmethod
    @abstractmethod
    def disable_configure_flag() -> str: ...
