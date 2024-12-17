# 只对afterrain做操作
import os

# 定义文件夹路径
visible_folder = r'D:\Desktop_Before\pix2pixHD-master\pix2pixHD\datasets\RGBT234\RGB_T234\afterrain\visible'
infrared_folder = r'D:\Desktop_Before\pix2pixHD-master\pix2pixHD\datasets\RGBT234\RGB_T234\afterrain\infrared'

# 获取两个文件夹中的文件列表
visible_files = os.listdir(visible_folder)
infrared_files = os.listdir(infrared_folder)

# 将文件名转换为集合，以便进行比较
visible_files_set = set(visible_files)
infrared_files_set = set(infrared_files)

# 找出不同时存在的文件，并删除
for file_name in visible_files_set.symmetric_difference(infrared_files_set):
    if file_name in visible_files_set:
        os.remove(os.path.join(visible_folder, file_name))
    if file_name in infrared_files_set:
        os.remove(os.path.join(infrared_folder, file_name))

print("delete unpaired completed!")


