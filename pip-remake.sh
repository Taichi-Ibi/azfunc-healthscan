#!/bin/sh

# 仮想環境がアクティブかどうかを確認
if [ -z "$VIRTUAL_ENV" ]; then
    echo "Error: No active virtual environment found."
    exit 1
fi

# packageをinstallし直す
pip freeze > uninstall.txt
pip uninstall -y -r uninstall.txt
pip install -r requirements.txt