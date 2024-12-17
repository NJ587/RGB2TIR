import pandas as pd

# 读取Excel文件
df = pd.read_excel("/home/huison/ai/every_catagory/metrics_output.xlsx")

# 处理FID列
def process_fid(fid_str):
    # 获取字符串中的数字部分
    fid_value = fid_str.split(":")[-1].strip()  # 提取冒号后面的部分，并去除空格
    return fid_value

# 应用处理函数到FID列
df['FID'] = df['FID'].apply(process_fid)

# 保存回Excel文件
df.to_excel("/home/huison/ai/every_catagory/metrics_output.xlsx", index=False)


import pandas as pd

# 读取Excel文件
df = pd.read_excel("/home/huison/ai/every_catagory/metrics_output.xlsx")

# 处理FID列
def process_fid(fid_str):
    # 获取字符串中的数字部分
    fid_value = fid_str.split(":")[-1].strip()  # 提取冒号后面的部分，并去除空格
    fid_value = fid_value.rstrip('}')  # 去除末尾的'}'符号
    return fid_value

# 应用处理函数到FID列
df['FID'] = df['FID'].apply(process_fid)

# 保存回Excel文件
df.to_excel("/home/huison/ai/every_catagory/metrics_output.xlsx", index=False)
