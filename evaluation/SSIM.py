import os
import cv2
import numpy as np
from skimage.metrics import structural_similarity

def calculate_ssim(folder1, folder2):
    """
    计算两个文件夹中所有图像的SSIM值。
    :param folder1: 第一个文件夹路径
    :param folder2: 第二个文件夹路径
    :return: None
    """
    # 获取文件夹中所有图像文件的路径
    images1 = [os.path.join(folder1, file) for file in os.listdir(folder1) if file.endswith('.jpg')]
    images2 = [os.path.join(folder2, file) for file in os.listdir(folder2) if file.endswith('.jpg')]

    # 确保两个文件夹中有相同数量的图像
    if len(images1) != len(images2):
        print("Error: 两个文件夹中图像数量不一致")
        return

    # 遍历图像并计算SSIM值
    total_ssim = 0
    for img1_path, img2_path in zip(images1, images2):
        img1 = cv2.imread(img1_path)
        img2 = cv2.imread(img2_path)

        # 转换图像为灰度图像
        gray_img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
        gray_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

        # 计算SSIM值
        ssim = structural_similarity(gray_img1, gray_img2)
        total_ssim += ssim

    # 计算平均SSIM值
    avg_ssim = total_ssim / len(images1)
    print(f"Average SSIM: {avg_ssim}")

# 测试函数
folder1 = "/home/huison/ai/total_real_and_fake/real_B/total/"
folder2 = "/home/huison/ai/total_real_and_fake/fake_B/total/"
calculate_ssim(folder1, folder2)
