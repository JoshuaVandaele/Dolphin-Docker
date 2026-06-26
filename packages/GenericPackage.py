from abc import ABC, abstractmethod


class GenericPackage(ABC):
    NAME: str

    @staticmethod
    @abstractmethod
    def debian() -> str: ...

    @staticmethod
    @abstractmethod
    def ubuntu() -> str: ...

    @staticmethod
    @abstractmethod
    def fedora() -> str: ...

    @staticmethod
    @abstractmethod
    def arch() -> str: ...

    @staticmethod
    @abstractmethod
    def alpine() -> str: ...

    @staticmethod
    @abstractmethod
    def gentoo() -> str: ...
