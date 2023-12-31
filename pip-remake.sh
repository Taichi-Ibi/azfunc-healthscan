#!/bin/sh

# 仮想環境がアクティブかどうかを確認
if [ ! -f "requirements.txt" ]; then
    echo "エラー！ requirements.txtが見つかりません"
    exit 1
fi

# requirements.txtが存在するか確認
if [ -z "$VIRTUAL_ENV" ]; then
    echo "エラー！ venvがアクティブになっていません。"
    exit 1
fi

# packageをinstallし直す
pip freeze > uninstall.txt
pip uninstall -y -r uninstall.txt
pip install -r requirements.txt

# uninstall.txtを.gitignoreに追加
echo '\n# pip-remake前のrequirements.txtを記載したファイル\nuninstall.txt' >> .gitignore