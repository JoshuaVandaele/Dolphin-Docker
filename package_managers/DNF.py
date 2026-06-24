from package_managers.GenericPackageManager import GenericPackageManager


class DNF(GenericPackageManager):
    @staticmethod
    def install(packages: list[str]) -> str:
        return f"dnf -y install {' '.join(packages)}"

    @staticmethod
    def apply_updates() -> str:
        return "dnf -y upgrade"

    @staticmethod
    def fetch_packages() -> str:
        return ""

    @staticmethod
    def clean() -> str:
        return "dnf clean all"
