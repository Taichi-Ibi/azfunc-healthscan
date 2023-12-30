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

# 実行
curl -sf https://raw.githubusercontent.com/Taichi-Ibi/azfunc-healthscan/main/pip-deps-check.py | python