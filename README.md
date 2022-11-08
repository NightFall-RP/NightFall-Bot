[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Discord](https://discordapp.com/api/guilds/837774112419479644/widget.png?style=shield)](https://discord.gg/cUXgZAxzvs)
####[日本語](https://github.com/NightFall-RP/Yotsubot/blob/dev/readme_ja.md)

# Hi there!
## This is Yotsubot, the official bot of NightFall. (A Ressurection of a old Project of mine.)

# Setup
As Long as you can edit a config files and use the terminal, you should be okay.

## Download Yotsubot's Codebase and reqirements onto your machine.
### (this implies you're using a linux terminal, with a apt package manager. which, if you are, you should already know how to do this, but I digress.)

```sh

# Clone the Yotsubot Repository
git clone https://github.com/NightFall-RP/Yotsubot

# Go Into the Yotsubot Folder
cd Yotsubot

# Since 3.9 isint really a native thing, we'll get it from deadsnakes.
sudo add-apt-repository ppa:deadsnakes

sudo apt install python 3.9-dev python3.9-distutils

# We'll get pip aswell.
wget https://bootstrap.pypa.io/get-pip.py
python3.9 get-pip.py && rm get-pip.py

# Then, we download dependencies;
python3.9 -m pip install -r requirements.txt

# Change Token in .env
sudo nano .env

# And Finally, Run.
python3.9 main.py

```
