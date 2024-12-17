% 定义要处理的文件夹路径
folder_path = 'E:\python_project\pix2pixHD-master\datasets\looklookme\train_B';

% 获取文件夹中所有图片的文件名
image_files = dir(fullfile(folder_path, '*.jpg')); % 假设所有图片都是jpg格式，如果有其他格式需要相应修改

% 遍历处理每张图片
for i = 1:length(image_files)
    % 拼接图片的完整路径
    image_path = fullfile(folder_path, image_files(i).name);
    
    % 读取图片
    img = imread(image_path);
    
    % 等比例调整大小为256x256
    img_resized = imresize(img, [256, 512]);
    
    % 保存调整大小后的图片
    imwrite(img_resized, image_path);
end
