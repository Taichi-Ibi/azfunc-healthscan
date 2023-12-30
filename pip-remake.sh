#!/bin/sh

# requirements.txtが存在するか確認
if [ ! -f "requirements.txt" ]; then
    echo "エラー！ requirements.txtが見つかりません"
    exit 1
fi

# 仮想環境がアクティブかどうかを確認
if [ -z "$VIRTUAL_ENV" ]; then
    echo "エラー！ venvがアクティブになっていません。"
    exit 1
fi

# packageをinstallし直す
pip freeze > uninstall.txt
pip uninstall -y -r uninstall.txt
pip install -r requirements.txt