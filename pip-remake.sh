#!/bin/sh

# packageをinstallし直す
pip freeze > uninstall.txt
pip uninstall -y -r uninstall.txt
pip install -r requirements.txt