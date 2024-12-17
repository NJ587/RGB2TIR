import os
import shutil
import re

# 定义要复制的类别及其对应的参数
categories = {
    "car4": {"start": 44, "step": 5},
    "walkingwoman": {"start": 44, "step": 15},
    "walkingmantiny": {"start": 44, "step": 2},
    "kite2": {"start": 44, "step": 83},
    "walkingtogether1": {"start": 44, "step": 18}
}

# 定义源路径和目标路径
source_dir = r'D:\Desktop_Before\pix2pixHD-master\pix2pixHD\datasets\RGBT234\infrared_116649'
target_dir = r'D:\Desktop_Before\pix2pixHD-master\pix2pixHD\datasets\RGBT234\test_B_630X460'
os.makedirs(target_dir, exist_ok=True)

# 遍历每个类别
for category, params in categories.items():
    start = params["start"]
    step = params["step"]
    
    # 构建正则表达式匹配模式
    pattern = re.compile(rf"{category}_(\d+).jpg")
    
    # 计数器，用于记录已复制的图片数量
    count = 0
    
    # 遍历源目录下的所有文件
    for filename in os.listdir(source_dir):
        # 使用正则表达式匹配文件名
        match = pattern.match(filename)
        if match:
            # 获取文件名中的数字部分
            number = int(match.group(1))
            
            # 检查数字是否符合要求
            if number >= start and (number - start) % step == 0:
                # 构建源文件路径和目标文件路径
                source_file = os.path.join(source_dir, filename)
                target_file = os.path.join(target_dir, filename)
                
                # 复制文件
                shutil.copyfile(source_file, target_file)
                
                # 增加计数器
                count += 1
                
                # 检查是否已经复制足够数量的图片
                if count >= 20:
                    break

print("test-B图片复制完成。")


import os
import shutil
import re

# 定义要复制的类别及其对应的参数
categories = {
    "car4": {"start": 44, "step": 5},
    "walkingwoman": {"start": 44, "step": 15},
    "walkingmantiny": {"start": 44, "step": 2},
    "kite2": {"start": 44, "step": 83},
    "walkingtogether1": {"start": 44, "step": 18}
}

# 定义源路径和目标路径
source_dir = r'D:\Desktop_Before\pix2pixHD-master\pix2pixHD\datasets\RGBT234\visible_116649'
target_dir = r'D:\Desktop_Before\pix2pixHD-master\pix2pixHD\datasets\RGBT234\test_A_630X460'
os.makedirs(target_dir, exist_ok=True)

# 遍历每个类别
for category, params in categories.items():
    start = params["start"]
    step = params["step"]
    
    # 构建正则表达式匹配模式
    pattern = re.compile(rf"{category}_(\d+).jpg")
    
    # 计数器，用于记录已复制的图片数量
    count = 0
    
    # 遍历源目录下的所有文件
    for filename in os.listdir(source_dir):
        # 使用正则表达式匹配文件名
        match = pattern.match(filename)
        if match:
            # 获取文件名中的数字部分
            number = int(match.group(1))
            
            # 检查数字是否符合要求
            if number >= start and (number - start) % step == 0:
                # 构建源文件路径和目标文件路径
                source_file = os.path.join(source_dir, filename)
                target_file = os.path.join(target_dir, filename)
                
                # 复制文件
                shutil.copyfile(source_file, target_file)
                
                # 增加计数器
                count += 1
                
                # 检查是否已经复制足够数量的图片
                if count >= 20:
                    break

print("test-B图片复制完成。")