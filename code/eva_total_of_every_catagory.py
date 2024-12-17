import os
import numpy as np
from PIL import Image
from tensorflow.keras.applications.inception_v3 import InceptionV3
from tensorflow.keras.applications.inception_v3 import preprocess_input
import cv2
from skimage.metrics import structural_similarity
import pandas as pd
import torch_fidelity

# FID 测量方法
def calculate_fid_score(fake_folder, real_folder):
    fid_scores = []
    for fake_subfolder, real_subfolder in zip(sorted(os.listdir(fake_folder)), sorted(os.listdir(real_folder))):
        fake_path = os.path.join(fake_folder, fake_subfolder)
        real_path = os.path.join(real_folder, real_subfolder)

        metrics_dict = torch_fidelity.calculate_metrics(
            input1=fake_path,
            input2=real_path,
            fid=True
        )
        fid_scores.append(metrics_dict)

    return fid_scores

# IS 测量方法
def calculate_is_score(fake_folder):
    is_scores = []
    # 加载预训练的InceptionV3模型
    inception_model = InceptionV3(include_top=False, weights='imagenet')

    for fake_subfolder in sorted(os.listdir(fake_folder)):
        fake_path = os.path.join(fake_folder, fake_subfolder)

        # 加载生成图像
        def load_images_from_folder(folder):
            images = []
            for filename in os.listdir(folder):
                img = Image.open(os.path.join(folder, filename))
                img = img.resize((299, 299))  # 将图像大小调整为InceptionV3所需的大小
                img = np.array(img)
                images.append(img)
            return np.array(images)

        # 加载生成图像
        fake_images = load_images_from_folder(fake_path)

        # 预处理图像数据
        fake_images = preprocess_input(fake_images)

        # 提取生成图像的特征
        fake_features = inception_model.predict(fake_images)

        # 平滑特征以避免零值
        epsilon = 1e-10
        fake_features += epsilon

        # 计算IS分数
        def calculate_is_score(features):
            preds = features.mean(axis=0)
            kl_divergence = (features * (np.log(features) - np.log(preds))).mean(axis=1)
            is_score = np.exp(kl_divergence.mean())
            return is_score

        fake_is_score = calculate_is_score(fake_features)
        is_scores.append(fake_is_score)

    return is_scores

# SSIM 测量方法
def calculate_ssim(folder1, folder2):
    ssim_scores = []
    for subfolder1, subfolder2 in zip(sorted(os.listdir(folder1)), sorted(os.listdir(folder2))):
        folder1_path = os.path.join(folder1, subfolder1)
        folder2_path = os.path.join(folder2, subfolder2)

        """
        计算两个文件夹中所有图像的SSIM值。
        :param folder1: 第一个文件夹路径
        :param folder2: 第二个文件夹路径
        :return: None
        """
        # 获取文件夹中所有图像文件的路径
        images1 = [os.path.join(folder1_path, file) for file in os.listdir(folder1_path) if file.endswith('.jpg')]
        images2 = [os.path.join(folder2_path, file) for file in os.listdir(folder2_path) if file.endswith('.jpg')]

        # 确保两个文件夹中有相同数量的图像
        if len(images1) != len(images2):
            print(f"Error: {subfolder1} and {subfolder2} have different numbers of images")
            continue

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
        ssim_scores.append(avg_ssim)

    return ssim_scores

if __name__ == "__main__":

    fake_folder = "/home/huison/ai/fake_B"
    real_folder = "/home/huison/ai/real_B"
    output_excel = "/home/huison/ai/metrics_output_fake_B_real_B.xlsx"

    # 计算FID、IS、SSIM分数
    fid_scores = calculate_fid_score(fake_folder, real_folder)
    is_scores = calculate_is_score(fake_folder)
    ssim_scores = calculate_ssim(real_folder, fake_folder)

    # 将结果存储到DataFrame中
    data = {
        '文件夹名': sorted(os.listdir(fake_folder)),
        'FID': fid_scores,
        'IS': is_scores,
        'SSIM': ssim_scores
    }

    # 将DataFrame转换为Excel文件
    df = pd.DataFrame(data)
    df.to_excel(output_excel, index=False)
