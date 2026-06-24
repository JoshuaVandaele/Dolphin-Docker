from abc import ABC, abstractmethod


class GenericPackageManager(ABC):
    @staticmethod
    @abstractmethod
    def install(packages: list[str]) -> str:
        pass

    @staticmethod
    @abstractmethod
    def apply_updates() -> str:
        pass

    @staticmethod
    @abstractmethod
    def fetch_packages() -> str:
        pass

    @staticmethod
    @abstractmethod
    def clean() -> str:
        pass
