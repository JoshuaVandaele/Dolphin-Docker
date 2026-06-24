import argparse
import os
import re
import subprocess

import tomllib

import distros
import packages
from distros.GenericDistro import GenericDistro
from Dockerfile import Dockerfile
from packages.GenericPackage import GenericPackage

with open("distros.toml", "rb") as f:
    config = tomllib.load(f)


def resolve_package(name: str) -> type[GenericPackage]:
    for pkg_name in dir(packages):
        cls = getattr(packages, pkg_name)
        if getattr(cls, "NAME", None) == name:
            return cls
    raise KeyError(f"No package registered for '{name}'.")


def resolve_packages(names: list[str]) -> list[type[GenericPackage]]:
    return [resolve_package(p) for p in names]


def resolve_distro(name: str) -> type[GenericDistro]:
    for distro in dir(distros):
        cls = getattr(distros, distro)
        if getattr(cls, "NAME", None) == name:
            return cls
    raise KeyError(f"No distro registered for '{name}'.")


def load_env():
    os.environ.update(config.pop("env", {}))


def load_distros() -> list[GenericDistro]:
    packages: dict[str, list[type[GenericPackage]]] = {
        "base": resolve_packages(config.pop("base", [])),
        "required": resolve_packages(config.pop("required", [])),
        "optional": resolve_packages(config.pop("optional", [])),
        "gcc": resolve_packages(config.pop("gcc", [])),
        "clang": resolve_packages(config.pop("clang", [])),
    }

    results = []
    for distro_name, distro_cfg in config.items():
        distro = resolve_distro(distro_name)
        quirks = distro_cfg.get("quirks", [])
        distro_packages = {
            **packages,
            "required": [p for p in packages["required"] if p.NAME not in quirks],
            "optional": [p for p in packages["optional"] if p.NAME not in quirks],
            "quirks": [p for p in packages["optional"] if p.NAME in quirks],
        }
        results.append(distro(**distro_packages))
    return results


def cmd_generate(args):
    output_dir = "Dockerfiles"
    os.makedirs(output_dir, exist_ok=True)
    for distro in load_distros():
        dockerfile = Dockerfile(distro).generate()
        filename = os.path.join(output_dir, f"{distro.NAME}.Dockerfile")
        with open(filename, "w") as f:
            f.write(dockerfile)
        print(f"Generated {filename}")


def parse_tests_from_dockerfile(dockerfile: str) -> list[str]:
    with open(dockerfile, "r") as f:
        contents = f.read()
    return re.findall(r"AS .+?-(.+)", contents, re.IGNORECASE)


def cmd_build(args):
    for distro in load_distros():
        if args.distro and args.distro != distro.NAME:
            continue
        dockerfile = os.path.join("Dockerfiles", f"{distro.NAME}.Dockerfile")
        tests = parse_tests_from_dockerfile(dockerfile)
        for test in tests:
            if args.test and args.test != test:
                continue
            target = f"{distro.NAME}-{test}"
            tag = f"DolphinDocker/{target}:latest"
            print(f"Building {tag}...")
            subprocess.run(
                [
                    "docker",
                    "build",
                    "-f",
                    dockerfile,
                    "-t",
                    tag,
                    "--target",
                    target,
                    ".",
                ],
                check=True,
            )


def cmd_run(args):
    for distro in load_distros():
        if args.distro and args.distro != distro.NAME:
            continue
        dockerfile = os.path.join("Dockerfiles", f"{distro.NAME}.Dockerfile")
        tests = parse_tests_from_dockerfile(dockerfile)
        for test in tests:
            if args.test and args.test != test:
                continue
            if "gcc" not in test and "clang" not in test:
                continue
            target = f"{distro.NAME}-{test}"
            tag = f"DolphinDocker/{target}:latest"
            out_dir = os.path.abspath(f"./out/{target}")
            os.makedirs(out_dir, exist_ok=True)
            print(f"Running {tag}...")
            subprocess.run(
                [
                    "docker",
                    "run",
                    "--rm",
                    "--shm-size=2g",
                    "-v",
                    f"{os.environ['DOLPHIN_DIR']}:/dolphin",
                    "-v",
                    f"{os.path.abspath('./ccache.conf')}:/etc/ccache.conf",
                    "-v",
                    f"{os.environ['CCACHE_DIR']}:/ccache",
                    tag,
                ],
                check=True,
            )


def main():
    parser = argparse.ArgumentParser(description="Manage distro Dockerfiles")
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("generate", help="Generate Dockerfiles from distros.toml")
    build_parser = subparsers.add_parser("build", help="Build a Docker image ")
    build_parser.add_argument(
        "distro",
        nargs="?",
        default=None,
        help="Distro name, e.g. alpine",
    )
    build_parser.add_argument(
        "test",
        nargs="?",
        default=None,
        help="Test name, e.g. alldeps-gcc",
    )

    run_parser = subparsers.add_parser("run", help="Run a Docker container")
    run_parser.add_argument(
        "distro",
        nargs="?",
        default=None,
        help="Distro name, e.g. alpine",
    )
    run_parser.add_argument(
        "test",
        nargs="?",
        default=None,
        help="Test name, e.g. alldeps-gcc",
    )

    args = parser.parse_args()

    load_env()

    {"generate": cmd_generate, "build": cmd_build, "run": cmd_run}[args.command](args)


if __name__ == "__main__":
    main()
