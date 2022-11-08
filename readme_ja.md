[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Discord](https://discordapp.com/api/guilds/837774112419479644/widget.png?style=shield)](https://discord.gg/cUXgZAxzvs)


# こんにちは!

## NightFallの公式ボット Yotsubotです。(私の昔のプロジェクトの再選考)


# セットアップ
設定ファイルの編集とターミナルが使えればOKです。

## Yotsubot のコードベースと必要なものをあなたのマシンにダウンロードします。

### (これは、Linuxのターミナルとaptパッケージマネージャを使っていることを意味します。もしそうなら、この方法はすでに知っているはずですが、余談です。)

```sh

# Yotsubot リポジトリをクローンする
git clone https://github.com/NightFall-RP/Yotsubot

# Yotsubot フォルダに入る
cd Yotsubot

# 3.9 は本当はネイティブではないので、deadsnakes から取得します。
sudo add-apt-repository ppa:deadsnakes

sudo apt install python 3.9-dev python3.9-distutils

# 私たちはpipも手に入れます。
wget https://bootstrap.pypa.io/get-pip.py
python3.9 get-pip.py && rm get-pip.py

# 次に、依存関係をダウンロードします。
python3.9 -m pip install -r requirements.txt

# .envの'Token'を変更する
sudo nano .env

# そして最後に、プログラムを実行します。
python3.9 main.py

```
