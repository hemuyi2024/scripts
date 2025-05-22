import pandas as pd
import csv  # 新增引入用于控制引号行为


# 设置 CSV 文件路径（请根据需要修改为你的实际路径）
csv_file_path = '/home/lty/datasets/RealUAV/city1/uav_infos.csv'
output_file_path = '/home/lty/datasets/RealUAV/city1/gt.txt'

# 读取 CSV 文件
# 读取 CSV 文件
df = pd.read_csv(csv_file_path)

# 打开目标文件，按格式写入经纬度数据
with open(output_file_path, 'w') as f:
    for lon, lat in zip(df['longitude'], df['latitude']):
        f.write(f"{lon}, {lat}\n")

print(f"经纬度已保存到：{output_file_path}")
