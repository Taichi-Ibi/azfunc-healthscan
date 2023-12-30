curl -sf "https://raw.githubusercontent.com/Taichi-Ibi/azfunc-healthscan/main/pip-remake.sh" | sh
if [ $? -ne 0 ]; then
    echo "Error in script execution"
    # ここにエラー発生時の処理を記述
fi
