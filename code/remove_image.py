import os
import shutil

# 定义源文件夹和目标文件夹路径
source_infrared_folder = r'D:\Desktop_Before\pix2pixHD-master\pix2pixHD\datasets\RGBT234\RGB_T234\afterrain\infrared'
target_infrared_folder = r'D:\Desktop_Before\pix2pixHD-master\pix2pixHD\datasets\RGBT234\infrared'

source_visible_folder = r'D:\Desktop_Before\pix2pixHD-master\pix2pixHD\datasets\RGBT234\RGB_T234\afterrain\visible'
target_visible_folder = r'D:\Desktop_Before\pix2pixHD-master\pix2pixHD\datasets\RGBT234\visible'

# 复制红外图像文件
for filename in os.listdir(source_infrared_folder):
    source_file_path = os.path.join(source_infrared_folder, filename)
    target_file_path = os.path.join(target_infrared_folder, filename)
    shutil.copyfile(source_file_path, target_file_path)

# 复制可见光图像文件
for filename in os.listdir(source_visible_folder):
    source_file_path = os.path.join(source_visible_folder, filename)
    target_file_path = os.path.join(target_visible_folder, filename)
    shutil.copyfile(source_file_path, target_file_path)

print("copy image completed!")
