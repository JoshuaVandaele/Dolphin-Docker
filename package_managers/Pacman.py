from package_managers.GenericPackageManager import GenericPackageManager


class Pacman(GenericPackageManager):
    @staticmethod
    def install(packages: list[str]) -> str:
        return f"pacman -S --noconfirm {' '.join(packages)}"

    @staticmethod
    def apply_updates() -> str:
        return "pacman -Syu --noconfirm"

    @staticmethod
    def fetch_packages() -> str:
        return "pacman -Sy --noconfirm"

    @staticmethod
    def clean() -> str:
        return "pacman -Scc --noconfirm"
