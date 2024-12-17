import os
import shutil

# 输入的两个文件夹路径
fake_folder = "E:\\python_project\\pix2pixHD-master\\results\\RGB_T234_step5\\fake_B"
real_folder = "E:\\python_project\\pix2pixHD-master\\results\\RGB_T234_step5\\real_B"

# 输出的两个子文件夹路径
fake_output_folder = "E:\\python_project\\pix2pixHD-master\\results\\RGB_T234_step5\\fake_B_every_catagory"
real_output_folder = "E:\\python_project\\pix2pixHD-master\\results\\RGB_T234_step5\\real_B_every_catagory"

# 获取两个文件夹中所有的图像文件名
fake_images = [f for f in os.listdir(fake_folder) if f.endswith('.jpg')]
real_images = [f for f in os.listdir(real_folder) if f.endswith('.jpg')]

# 找到两个文件夹中共同的图像文件名
common_images = set(fake_images).intersection(real_images)

# 遍历每一个共同的图像文件名，进行复制操作
for img_name in common_images:
    # 创建对应的子文件夹
    img_folder_name = img_name.replace('.jpg', '')
    fake_img_folder = os.path.join(fake_output_folder, img_folder_name)
    real_img_folder = os.path.join(real_output_folder, img_folder_name)
    
    os.makedirs(fake_img_folder, exist_ok=True)
    os.makedirs(real_img_folder, exist_ok=True)
    
    # 复制图片到对应的子文件夹
    fake_img_path = os.path.join(fake_folder, img_name)
    real_img_path = os.path.join(real_folder, img_name)
    
    shutil.copy(fake_img_path, fake_img_folder)
    shutil.copy(real_img_path, real_img_folder)

print("复制完成!")
