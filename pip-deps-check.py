import logging
import os
import re
import subprocess

PATH = "requirements.txt"


def check_requirements_with_pip_show(requirements_path):
    # requirements.txt ファイルを読み込む
    with open(requirements_path, "r") as file:
        lines = set(line.strip() for line in file if line.strip())
    required_packages = set(
        line.split("==")[0] for line in lines if not line.startswith("#")
    )

    # 依存関係にあるパッケージをチェックするためのセット
    dependencies = set()

    # 各パッケージに対して pip show を実行し、依存関係を取得
    for package in required_packages:
        output = subprocess.check_output(
            ["pip", "show", package], stderr=subprocess.STDOUT
        ).decode("utf-8")
        # Requires で始まる行を見つけ、依存関係を抽出
        match = re.search(r"^Requires: (.+)$", output, re.MULTILINE)
        if match:
            deps = match.group(1).split(", ")
            dependencies.update(deps)

    # requirements.txt にない依存パッケージを識別
    missing_packages = dependencies - required_packages
    if missing_packages:
        message = "依存パッケージの記載漏れが見つかりました。以下のパッケージのインストールを試してみてください。\n{missing_packages}".format(
            missing_packages=os.linesep.join(missing_packages)
        )
        logging.warning(message)


# 依存関係のチェックを実行
check_requirements_with_pip_show(requirements_path=PATH)
