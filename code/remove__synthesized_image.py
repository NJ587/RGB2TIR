import os

def rename_images(directory):
    # 遍历目录中的文件
    for filename in os.listdir(directory):
        if filename.endswith("_synthesized_image.jpg"):
            # 构建新的文件名
            new_filename = filename.replace("_synthesized_image", "")
            # 构建旧的文件路径和新的文件路径
            old_path = os.path.join(directory, filename)
            new_path = os.path.join(directory, new_filename)
            # 重命名文件
            os.rename(old_path, new_path)

# 指定目标文件夹路径
directory = "/data_F/lina/python_project/pix2pixHD-master/results/RGB_T234_step5/fake_B"

# 执行重命名操作
rename_images(directory)
