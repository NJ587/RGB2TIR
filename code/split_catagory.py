import os
import shutil

# 定义路径
source_dir = r'D:\Desktop_Before\pix2pixHD-master\pix2pixHD\results\RGBT234_nocrop\fake_B'
destination_dir = r'D:\Desktop_Before\pix2pixHD-master\pix2pixHD\results\RGBT234_nocrop\fake_B_every_catagory'

# 获取所有文件名
file_names = os.listdir(source_dir)

# 创建目标文件夹
os.makedirs(destination_dir, exist_ok=True)

# 遍历所有文件
for file_name in file_names:
    # 提取字符串部分
    category = file_name.split('_')[0]
    
    # 构建目标文件夹路径
    category_dir = os.path.join(destination_dir, category)
    
    # 创建目标文件夹
    os.makedirs(category_dir, exist_ok=True)
    
    # 构建源文件路径和目标文件路径
    source_file_path = os.path.join(source_dir, file_name)
    destination_file_path = os.path.join(category_dir, file_name)
    
    # 复制文件
    shutil.copy(source_file_path, destination_file_path)

print("fake_B文件分类和复制完成！")


# 定义路径
source_dir = r'D:\Desktop_Before\pix2pixHD-master\pix2pixHD\results\RGBT234_nocrop\real_B'
destination_dir = r'D:\Desktop_Before\pix2pixHD-master\pix2pixHD\results\RGBT234_nocrop\real_B_every_catagory'

# 获取所有文件名
file_names = os.listdir(source_dir)

# 创建目标文件夹
os.makedirs(destination_dir, exist_ok=True)

# 遍历所有文件
for file_name in file_names:
    # 提取字符串部分
    category = file_name.split('_')[0]
    
    # 构建目标文件夹路径
    category_dir = os.path.join(destination_dir, category)
    
    # 创建目标文件夹
    os.makedirs(category_dir, exist_ok=True)
    
    # 构建源文件路径和目标文件路径
    source_file_path = os.path.join(source_dir, file_name)
    destination_file_path = os.path.join(category_dir, file_name)
    
    # 复制文件
    shutil.copy(source_file_path, destination_file_path)

print("real_B文件分类和复制完成！")
