import os
import shutil
from collections import defaultdict

# 源路径和目标路径
source_dir = r'D:\Desktop_Before\pix2pixHD-master\pix2pixHD\datasets\RGBT234\infrared_116649'
target_dir = r'D:\Desktop_Before\pix2pixHD-master\pix2pixHD\datasets\RGBT234\infrared_11700'

# 创建目标路径文件夹（如果不存在）
if not os.path.exists(target_dir):
    os.makedirs(target_dir)

# 读取源文件夹中的所有文件名
files = os.listdir(source_dir)

# 使用 defaultdict 来建立类别到文件列表的映射
class_to_files = defaultdict(list)

for filename in files:
    # 提取类别字符串
    class_name = filename.split('_')[0]
    class_to_files[class_name].append(filename)

# 每个类别复制50张图片到目标路径
for class_name, filenames in class_to_files.items():
    # 随机选择50张图片
    selected_files = filenames[:50]
    
    # 复制图片到目标路径
    for filename in selected_files:
        source_file = os.path.join(source_dir, filename)
        target_file = os.path.join(target_dir, filename)
        shutil.copyfile(source_file, target_file)
