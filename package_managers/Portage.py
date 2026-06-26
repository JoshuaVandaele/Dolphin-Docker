from package_managers.GenericPackageManager import GenericPackageManager


class Portage(GenericPackageManager):
    @staticmethod
    def install(packages: list[str]) -> str:
        package_list = " ".join(packages)
        return f"emerge --autounmask-write --autounmask-backtrack=y {package_list} ; etc-update --automode -5 && emerge {package_list}"

    @staticmethod
    def apply_updates() -> str:
        return "emerge --update --deep --newuse @world"

    @staticmethod
    def fetch_packages() -> str:
        return "emerge-webrsync"

    @staticmethod
    def clean() -> str:
        return "emerge --depclean"
