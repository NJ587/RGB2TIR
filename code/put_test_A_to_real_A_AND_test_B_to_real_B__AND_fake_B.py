#1）将D:\Desktop_Before\pix2pixHD-master\pix2pixHD\results\RGBT234_20000\test_latest\images下命名中有'_synthesized_image.jpg'的图片复制到D:\Desktop_Before\pix2pixHD-master\pix2pixHD\results\RGBT234_20000\fake_B中，
#2）将D:\Desktop_Before\pix2pixHD-master\pix2pixHD\datasets\RGBT234_20000\test_A中所有图片复制到D:\Desktop_Before\pix2pixHD-master\pix2pixHD\results\RGBT234_20000\real_A中，
#3）将D:\Desktop_Before\pix2pixHD-master\pix2pixHD\datasets\RGBT234_20000\test_B中所有图片复制到D:\Desktop_Before\pix2pixHD-master\pix2pixHD\results\RGBT234_20000\real_B中，


import os
import shutil

def copy_images_with_keyword(source_directory, destination_directory, keyword):
    # 创建目标文件夹（如果不存在）
    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)
    
    # 遍历源目录中的文件
    for filename in os.listdir(source_directory):
        if filename.endswith(keyword):
            source_path = os.path.join(source_directory, filename)
            destination_path = os.path.join(destination_directory, filename)
            shutil.copyfile(source_path, destination_path)

# 第一个任务：复制带有'_synthesized_image.jpg'关键字的图像到fake_B文件夹中
source_directory_1 = "/data_F/lina/python_project/pix2pixHD-master/results/RGB_T234_step5/test_latest/images"
destination_directory_1 = "/data_F/lina/python_project/pix2pixHD-master/results/RGB_T234_step5/fake_B"
copy_images_with_keyword(source_directory_1, destination_directory_1, "_synthesized_image.jpg")

# 第二个任务：复制test_A文件夹中的所有图像到real_A文件夹中
source_directory_2 = "/data_F/lina/python_project/pix2pixHD-master/datasets/step_5_of_top100/test_A"
destination_directory_2 = "/data_F/lina/python_project/pix2pixHD-master/results/RGB_T234_step5/real_A"
shutil.copytree(source_directory_2, destination_directory_2)

# 第三个任务：复制test_B文件夹中的所有图像到real_B文件夹中
source_directory_3 = "/data_F/lina/python_project/pix2pixHD-master/datasets/step_5_of_top100/test_B"
destination_directory_3 = "/data_F/lina/python_project/pix2pixHD-master/results/RGB_T234_step5/real_B_512X256"
shutil.copytree(source_directory_3, destination_directory_3)
