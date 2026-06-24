class DockerSection:
    DOLPHIN_DIR = "/dolphin"

    def __init__(self, base, target):
        self.base = base
        self.target = target

    def __str__(self):
        return f"""FROM {self.base} AS {self.target}"""


class DockerBaseSection(DockerSection):
    def __init__(self, base, target):
        super().__init__(base, target)
        self.package_manager = None
        self.base_packages = None

    def __str__(self):
        return (
            f"{super().__str__()}\n\n"
            f"RUN {self.package_manager} {self.base_packages}"
            f"RUN git config --global --add safe.directory {self.DOLPHIN_DIR}"
            "COPY entrypoint.sh /entrypoint.sh"
            "RUN chmod +x /entrypoint.sh"
            'ENTRYPOINT ["/entrypoint.sh"]'
        )


class DockerNoDepsSection(DockerSection):
    def __init__(self, base, target):
        super().__init__(base, target)

    def __str__(self):
        return f"""FROM {self.base} AS {self.target}"""


class DockerBuilder:
    def __init__(self, name, base):
        self.name = name
        self.base = base
        self.sections = [
            DockerBaseSection(f"{base}:latest", f"{name}-base"),
            DockerNoDepsSection(f"{name}-base", f"{name}-nodeps"),
            DockerSection(f"{name}-nodeps", f"{name}-nodeps-gcc"),
            DockerSection(f"{name}-nodeps", f"{name}-nodeps-clang"),
            DockerSection(f"{name}-nodeps", f"{name}-alldeps"),
            DockerSection(f"{name}-alldeps", f"{name}-alldeps-gcc"),
            DockerSection(f"{name}-alldeps", f"{name}-alldeps-clang"),
        ]


def main():
    alpine_builder = DockerBuilder("alpine", "alpine:latest")


if __name__ == "__main__":
    main()
