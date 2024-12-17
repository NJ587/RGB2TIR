import os

def rename_files(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".jpg"):
            split_name = filename.split("_")
            base_name = split_name[1].split(".")[0]  # 获取文件名中的基本部分，去除扩展名
            new_filename = f"{base_name}_{split_name[0]}.jpg"
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
            print(f"Renamed {filename} to {new_filename}")

directory = r"D:\Desktop_Before\pix2pixHD-master\pix2pixHD\datasets\RGBT234\infrared_116649"
rename_files(directory)
