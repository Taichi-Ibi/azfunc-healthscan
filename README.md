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
ローカルのvenvに手動で```pip install```したパッケージを削除して、開発とデプロイの環境を一致させる
#### 処理手順
- venv内の全パッケージを出力
- 出力した全パッケージをアンインストール
- requirements.txtに記載のあるパッケージを再インストール  
#### 実行手順
デプロイするディレクトリのルートでvenvを起動させた状態でTerminalにてコマンドを実行する
```Shell
curl -sf https://raw.githubusercontent.com/Taichi-Ibi/pipclean/main/pip-remake.sh | sh
```  
#### その他
- コマンド実行後に生成されるuninstall.txtは.gitignoreに追記される。不要であれば削除してよい
### 2. requirements.txt内の依存関係を確認
requirements.txtに記載されていない依存パッケージを表示する
#### 処理手順
- 全パッケージに対して```pip show```を実行して依存パッケージを取得する
- requirements.txtに記載されていない依存パッケージを表示する
#### 実行手順
デプロイするディレクトリのルートでvenvを起動させた状態でTerminalにてコマンドを実行する
```Shell
curl -sf https://raw.githubusercontent.com/Taichi-Ibi/pipclean/main/pip-deps-check.sh | sh
```  
#### その他
- requirements.txtに全てのパッケージを記載する必要はないが、Azure Functionsでは依存パッケージを明示的にインストール必要な場合がある