import os
import shutil

def copy_images_by_category(source_directory, destination_directory, max_images_per_category=5):
    # 创建目标文件夹（如果不存在）
    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)
    
    # 统计每个类别的图像数量
    category_counts = {}
    for filename in os.listdir(source_directory):
        if filename.endswith(".jpg"):
            category = filename.split("_")[0]  # 提取类别名
            if category not in category_counts:
                category_counts[category] = []
            if len(category_counts[category]) < max_images_per_category:
                category_counts[category].append(filename)
    
    # 复制图像到目标文件夹
    for category, filenames in category_counts.items():
        for filename in filenames:
            source_path = os.path.join(source_directory, filename)
            destination_path = os.path.join(destination_directory, filename)
            shutil.copyfile(source_path, destination_path)

source_directory = r"D:\Desktop_Before\pix2pixHD-master\pix2pixHD\datasets\RGBT234\infrared_116649"
destination_directory = r"D:\Desktop_Before\pix2pixHD-master\pix2pixHD\datasets\RGBT234\test_B"
copy_images_by_category(source_directory, destination_directory, max_images_per_category=5)


source_directory = r"D:\Desktop_Before\pix2pixHD-master\pix2pixHD\datasets\RGBT234\visible_116649"
destination_directory = r"D:\Desktop_Before\pix2pixHD-master\pix2pixHD\datasets\RGBT234\test_A"
copy_images_by_category(source_directory, destination_directory, max_images_per_category=5)