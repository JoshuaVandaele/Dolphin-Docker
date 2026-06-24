from package_managers.GenericPackageManager import GenericPackageManager


class APK(GenericPackageManager):
    @staticmethod
    def install(packages: list[str]) -> str:
        return f"apk add --no-cache {' '.join(packages)}"

    @staticmethod
    def apply_updates() -> str:
        return "apk update"

    @staticmethod
    def fetch_packages() -> str:
        return "apk upgrade"

    @staticmethod
    def clean() -> str:
        return "rm -rf /var/cache/apk/*"
