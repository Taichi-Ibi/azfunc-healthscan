## About azfunc-healthscan
### 背景
必要なパッケージのインストール漏れにより、Azure Functionsに関数が表示されなかったり、関数実行時に500エラーを吐いたりする
### 目的
Azure Functionsにデプロイする環境の状態をチェックする
### 課題
- requirements.txtへのパッケージ記載漏れ
    - ローカルのvenvに手動で```pip install```したパッケージ
    - 依存関係にあるパッケージ
## Usage
### 1. venv内のパッケージ初期化
ローカルのvenvに手動で```pip install```したパッケージを削除する
#### 処理手順
- venv内の全パッケージを出力
- 出力した全パッケージをアンインストール
- requirements.txtに記載のあるパッケージを再インストール  
#### 実行手順
デプロイするディレクトリのルートでvenvを起動させた状態でTerminalにてコマンドを実行する
```Shell
curl https://raw.githubusercontent.com/Taichi-Ibi/azfunc-healthscan/main/pip-remake.sh
```  
#### その他
- コマンド実行後に生成されるuninstall.txtは不要であれば削除してよい