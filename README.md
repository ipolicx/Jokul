# Jokul
# A wallpaper app that changes hourly
#
# Install PyInstaller
# Use the official PyPI source to install PyInstaller
pip install pyinstaller
#
# Use the Tsinghua University mirror to install PyInstaller for faster download
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pyinstaller
#
# Use PyInstaller to package jokul.py into a single .exe file and include the resources in the Images folder
pyinstaller --onefile --add-data "Images;Images" jokul.py
