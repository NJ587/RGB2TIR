import os
from collections import defaultdict

# 图片所在路径
images_dir = r'D:\Desktop_Before\pix2pixHD-master\pix2pixHD\datasets\RGBT234_20000\train_A'

# 获取路径下所有文件
image_files = os.listdir(images_dir)

# 使用 defaultdict 来建立类别到文件数量的映射
class_to_count = defaultdict(int)

# 遍历每个文件，计算每一类有多少张图片
for filename in image_files:
    # 获取类别字符串
    class_name = filename.split('_')[1].split('.')[0]
    # 增加对应类别的图片数量
    class_to_count[class_name] += 1

# 打印每一类有多少张图片
for class_name, count in class_to_count.items():
    print(f"类别 '{class_name}' 有 {count} 张图片.")
