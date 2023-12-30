import logging
import os
import re
import subprocess
import sys

PATH = "requirements.txt"


def simple_progress_bar(current, total, bar_length=50):
    fraction = current / total
    arrow = int(fraction * bar_length - 1) * "-" + ">"
    padding = int(bar_length - len(arrow)) * " "
    sys.stdout.write(
        f"\r\033[34mProgress: [{arrow}{padding}] {int(fraction * 100)}%\033[0m"
    )
    sys.stdout.flush()


def get_package_dependencies(package):
    try:
        output = subprocess.check_output(
            ["pip", "show", package], stderr=subprocess.STDOUT
        ).decode("utf-8")
        match = re.search(r"^Requires: (.+)$", output, re.MULTILINE)
        if match:
            return set(match.group(1).split(", "))
    except subprocess.CalledProcessError:
        print()
        logging.error(f"エラー！ パッケージ '{package}' が見つかりませんでした。インストールされているか確認してください。")
        exit(1)
    return set()


def check_requirements_with_pip_show(requirements_path):
    with open(requirements_path, "r") as file:
        lines = set(line.strip() for line in file if line.strip())
    required_packages = [
        (line.split("==")[0], None) for line in lines if not line.startswith("#")
    ]

    dependencies = set()
    total_packages = len(required_packages)

    for i, (package, _) in enumerate(required_packages, 1):
        deps = get_package_dependencies(package)
        required_packages[i - 1] = (package, deps)
        dependencies.update(deps)
        simple_progress_bar(i, total_packages)

    sys.stdout.write("\n")
    sys.stdout.flush()

    missing_packages = dependencies - set(pkg for pkg, _ in required_packages)
    if missing_packages:
        message = "依存パッケージの記載漏れが見つかりました。以下のパッケージのインストールを試してみてください。\n{missing_packages}".format(
            missing_packages=os.linesep.join(missing_packages)
        )
        logging.warning(message)


check_requirements_with_pip_show(requirements_path=PATH)
