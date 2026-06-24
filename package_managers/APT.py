from package_managers.GenericPackageManager import GenericPackageManager


class APT(GenericPackageManager):
    @staticmethod
    def install(packages: list[str]) -> str:
        return f"apt-get install -y {' '.join(packages)}"

    @staticmethod
    def apply_updates() -> str:
        return "apt-get update"

    @staticmethod
    def fetch_packages() -> str:
        return "apt-get upgrade -y"

    @staticmethod
    def clean() -> str:
        return "rm -rf /var/cache/apt/archives /var/lib/apt/lists/*"
