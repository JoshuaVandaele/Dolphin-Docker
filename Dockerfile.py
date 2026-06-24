from abc import ABCMeta

import packages
from distros.GenericDistro import GenericDistro
from packages.GenericOptionalPackage import GenericOptionalPackage


class Dockerfile:
    DOLPHIN_DIR = "/dolphin"

    def __init__(self, distro: GenericDistro) -> None:
        self.distro = distro

    def _install_stages(self, stages: list[str]) -> str:
        return (
            (
                f"RUN {self.distro.PACKAGE_MANAGER.fetch_packages()}\n"
                if self.distro.PACKAGE_MANAGER.fetch_packages()
                else ""
            )
            + f"RUN {self.distro.PACKAGE_MANAGER.apply_updates()}\n"
            + f"RUN {self.distro.PACKAGE_MANAGER.install([p for stage in stages for p in self.distro.packages[stage]])}\n"
            + f"RUN {self.distro.PACKAGE_MANAGER.clean()}\n"
        )

    def _gcc(self) -> str:
        return self._install_stages(["gcc"]) + "ENV CC=gcc\n" + "ENV CXX=g++\n"

    def _clang(self) -> str:
        return (
            self._install_stages(["clang"])
            + "ENV CC=clang\n"
            + "ENV CXX=clang++\n"
            + 'ENV LDFLAGS="-fuse-ld=lld"\n'
        )

    @staticmethod
    def _make_cmake_env(args):
        return 'ENV CMAKE_ARGS="' + " ".join(args) + '"\n'

    def _quirks(self) -> str:
        if not self.distro.packages["quirks"]:
            return ""
        return Dockerfile._make_cmake_env(q for q in self.distro.packages["quirks"])

    @staticmethod
    def _min_packages_flag() -> str:
        flags = []
        for pkg_name in dir(packages):
            cls = getattr(packages, pkg_name)
            if (
                isinstance(cls, ABCMeta)
                and issubclass(cls, GenericOptionalPackage)
                and pkg_name != "GenericOptionalPackage"
            ):
                flags.append(cls.disable_configure_flag())

        return Dockerfile._make_cmake_env(flags)

    def generate(self) -> str:
        return (
            f"FROM {self.distro.IMAGE} AS {self.distro.NAME}-base\n"
            + self._install_stages(["base"])
            + f"RUN git config --global --add safe.directory {self.DOLPHIN_DIR}\n"
            + self._quirks()
            + "COPY entrypoint.sh /entrypoint.sh\n"
            + "RUN chmod +x /entrypoint.sh\n"
            + 'ENTRYPOINT ["/entrypoint.sh"]\n'
            + "\n"
            + f"FROM {self.distro.NAME}-base AS {self.distro.NAME}-nodeps\n"
            + "ENV USE_SYSTEM_LIBS=OFF\n"
            + self._min_packages_flag()
            + "\n"
            + f"FROM {self.distro.NAME}-nodeps AS {self.distro.NAME}-nodeps-gcc\n"
            + self._gcc()
            + "\n"
            + f"FROM {self.distro.NAME}-nodeps AS {self.distro.NAME}-nodeps-clang\n"
            + self._clang()
            + "\n"
            + f"FROM {self.distro.NAME}-base AS {self.distro.NAME}-alldeps\n"
            + self._install_stages(["required", "optional"])
            + "ENV USE_SYSTEM_LIBS=ON\n"
            + "\n"
            + f"FROM {self.distro.NAME}-alldeps AS {self.distro.NAME}-alldeps-gcc\n"
            + self._gcc()
            + "\n"
            + f"FROM {self.distro.NAME}-alldeps AS {self.distro.NAME}-alldeps-clang\n"
            + self._clang()
        )
