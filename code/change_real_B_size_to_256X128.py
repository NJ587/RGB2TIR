from PIL import Image
import os

# 定义输入和输出文件夹路径
input_folder = '/data_F/lina/python_project/pix2pixHD-master/results/RGB_T234_step5/real_B_512X256'
output_folder = '/data_F/lina/python_project/pix2pixHD-master/results/RGB_T234_step5/real_B'

# 确保输出文件夹存在，如果不存在则创建
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 循环处理输入文件夹中的每张图片
for filename in os.listdir(input_folder):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        # 打开图片
        image_path = os.path.join(input_folder, filename)
        image = Image.open(image_path)
        
        # 调整图片尺寸为256x128
        resized_image = image.resize((256, 128))
        
        # 构造输出路径
        output_path = os.path.join(output_folder, filename)
        
        # 保存调整尺寸后的图片
        resized_image.save(output_path)

print("real_图片转换完成！")



