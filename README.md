
# Jokul

### 项目简介 / Project Introduction

Jokul 是一个配合Windows任务计划，整点换壁纸每小时更换桌面壁纸的应用程序。

Jokul is a wallpaper application that changes your desktop background hourly.

### 安装 / Installation

### 前置条件 / Prerequisites

- 系统已安装 Python 3.x。/ Python 3.x installed on your system.
- 确保你已经安装了 `pip`，大多数 Python 发行版都自带 `pip`。/ Ensure you have `pip` installed, which comes with most Python distributions.

### 安装 PyInstaller / Install PyInstaller

你可以使用官方的 PyPI 源来安装 `PyInstaller`：/ You can install `PyInstaller` using the official PyPI source:

```sh
pip install pyinstaller
```

或者，为了加快下载速度，你可以使用清华大学的镜像源：/ Alternatively, for faster download speeds, you can use the Tsinghua University mirror:

```sh
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pyinstaller
```

### 使用 / Usage

要将 `jokul.py` 打包成一个单独的可执行文件并包含 `Images` 文件夹中的资源，运行以下命令：/ To package `jokul.py` into a single executable file and include the resources in the `Images` folder, run the following command:

```sh
pyinstaller --onefile --add-data "Images;Images" --noconsole jokul.py
```

这将在 `dist` 目录中生成一个单个的 `.exe` 文件。 

This command will generate a single `.exe` file in the `dist` directory.

### 运行应用 / Running the Application

1. 导航到生成的 `.exe` 文件所在的 `dist` 目录。/ Navigate to the `dist` directory where the `.exe` file is located.
2. 双击 `jokul.exe` 文件运行应用程序。/ Double-click the `jokul.exe` file to run the application.

### 功能 / Features

- 每小时自动更换桌面壁纸。 / Automatically changes the desktop wallpaper every hour.
- 支持存储在 `Images` 文件夹中的自定义壁纸图像。/ Supports custom wallpaper images stored in the `Images` folder.

### 目录结构 / Directory Structure

```
Jokul/
├── jokul.py
├── Images/
│   ├── jokul_100.jpg
│   ├── jokul_101.jpg
│   └── ...
└── wallpapers.log
```

### 日志 / Logging

应用程序将其活动记录到与脚本位于同一目录下的 `wallpapers.log` 文件中。此日志文件有助于调试和跟踪应用程序的行为。

The application logs its activities to `wallpapers.log` in the same directory as the script. This log file helps in debugging and tracking the application's behavior.

---

感谢您使用 Jokul！/ Thank you for using Jokul!


