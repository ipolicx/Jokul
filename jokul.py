import os
import ctypes
import logging
from datetime import datetime, timedelta
from pathlib import Path

# 获取脚本所在文件夹
script_dir = Path(__file__).parent

# 日志文件路径设置为与脚本在同一文件夹
log_file_path = os.path.join(script_dir, "wallpapers.log")

# 日志级别和格式设置
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s: %(levelname)s: %(message)s')

# 添加文件处理器到日志系统
handler = logging.FileHandler(log_file_path)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s')
handler.setFormatter(formatter)
logging.getLogger('').addHandler(handler)

SPI_SETDESKWALLPAPER = 0x0014

def set_wallpaper(hour, wallpaper_folder):
    """设置壁纸"""
    wallpaper_filename = f"jokul_1{hour:02d}.jpg"
    wallpaper_path = os.path.join(wallpaper_folder, wallpaper_filename)

    logging.debug(f"Attempting to set wallpaper at: {wallpaper_path}")
    if os.path.exists(wallpaper_path):
        try:
            result = ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, wallpaper_path, 0)
            if result:
                logging.info("Wallpaper changed successfully.")
            else:
                logging.error("Failed to change wallpaper.")
        except FileNotFoundError:
            logging.error(f"Wallpaper file not found: {wallpaper_path}")
        except Exception as e:
            logging.error(f"Error changing wallpaper: {e}")
    else:
        logging.warning(f"No wallpaper found for the hour: {hour}")

def change_wallpaper(hour=None):
    """根据给定的小时数设置壁纸，如果未提供则使用当前小时"""
    if hour is None:
        hour = datetime.now().hour
    images_path = os.path.join(script_dir, "Images")
    set_wallpaper(hour, images_path)

def main():
    """脚本入口点"""
    change_wallpaper()

if __name__ == "__main__":
    main()