from PIL import Image
import os

# 定义输入和输出文件夹路径
input_folder = r'D:\Desktop_Before\pix2pixHD-master\pix2pixHD\datasets\RGBT234\step_5_of_top100\test_A_630X460'
output_folder = r'D:\Desktop_Before\pix2pixHD-master\pix2pixHD\datasets\RGBT234\step_5_of_top100\test_A'

# 确保输出文件夹存在，如果不存在则创建
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 循环处理输入文件夹中的每张图片
for filename in os.listdir(input_folder):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        # 打开图片
        image_path = os.path.join(input_folder, filename)
        image = Image.open(image_path)
        
        # 调整图片尺寸为512x256
        resized_image = image.resize((512, 256))
        
        # 构造输出路径
        output_path = os.path.join(output_folder, filename)
        
        # 保存调整尺寸后的图片
        resized_image.save(output_path)

print("test_A图片转换完成！")


# 定义输入和输出文件夹路径
input_folder = r'D:\Desktop_Before\pix2pixHD-master\pix2pixHD\datasets\RGBT234\step_5_of_top100\test_B_630X460'
output_folder = r'D:\Desktop_Before\pix2pixHD-master\pix2pixHD\datasets\RGBT234\step_5_of_top100\test_B'

# 确保输出文件夹存在，如果不存在则创建
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 循环处理输入文件夹中的每张图片
for filename in os.listdir(input_folder):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        # 打开图片
        image_path = os.path.join(input_folder, filename)
        image = Image.open(image_path)
        
        # 调整图片尺寸为512x256
        resized_image = image.resize((512, 256))
        
        # 构造输出路径
        output_path = os.path.join(output_folder, filename)
        
        # 保存调整尺寸后的图片
        resized_image.save(output_path)

print("test_B图片转换完成！")


# 定义输入和输出文件夹路径
input_folder = r'D:\Desktop_Before\pix2pixHD-master\pix2pixHD\datasets\RGBT234\step_5_of_top100\train_B_630X460'
output_folder = r'D:\Desktop_Before\pix2pixHD-master\pix2pixHD\datasets\RGBT234\step_5_of_top100\train_B'

# 确保输出文件夹存在，如果不存在则创建
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 循环处理输入文件夹中的每张图片
for filename in os.listdir(input_folder):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        # 打开图片
        image_path = os.path.join(input_folder, filename)
        image = Image.open(image_path)
        
        # 调整图片尺寸为512x256
        resized_image = image.resize((512, 256))
        
        # 构造输出路径
        output_path = os.path.join(output_folder, filename)
        
        # 保存调整尺寸后的图片
        resized_image.save(output_path)

print("train_B图片转换完成！")

# 定义输入和输出文件夹路径
input_folder = r'D:\Desktop_Before\pix2pixHD-master\pix2pixHD\datasets\RGBT234\step_5_of_top100\train_A_630X460'
output_folder = r'D:\Desktop_Before\pix2pixHD-master\pix2pixHD\datasets\RGBT234\step_5_of_top100\train_A'

# 确保输出文件夹存在，如果不存在则创建
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 循环处理输入文件夹中的每张图片
for filename in os.listdir(input_folder):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        # 打开图片
        image_path = os.path.join(input_folder, filename)
        image = Image.open(image_path)
        
        # 调整图片尺寸为512x256
        resized_image = image.resize((512, 256))
        
        # 构造输出路径
        output_path = os.path.join(output_folder, filename)
        
        # 保存调整尺寸后的图片
        resized_image.save(output_path)

print("train_A图片转换完成！")
