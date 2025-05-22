import re
import math
from osgeo import osr

def euler_to_quaternion(yaw, pitch, roll):
    """
    将欧拉角（单位：度）转换为四元数
    顺序：Z（yaw）-> Y（pitch）-> X（roll）
    """
    # 转换为弧度
    yaw_rad = math.radians(yaw)
    pitch_rad = math.radians(pitch)
    roll_rad = math.radians(roll)

    cy = math.cos(yaw_rad * 0.5)
    sy = math.sin(yaw_rad * 0.5)
    cp = math.cos(pitch_rad * 0.5)
    sp = math.sin(pitch_rad * 0.5)
    cr = math.cos(roll_rad * 0.5)
    sr = math.sin(roll_rad * 0.5)

    qw = cr * cp * cy + sr * sp * sy
    qx = sr * cp * cy - cr * sp * sy
    qy = cr * sp * cy + sr * cp * sy
    qz = cr * cp * sy - sr * sp * cy

    return qx, qy, qz, qw

def extract_tum_with_quaternion(srt_file_path, output_file_path):
    """
    提取经纬度、高度和相机姿态信息（转四元数），保存为TUM格式
    """
    try:
        with open(srt_file_path, 'r', encoding='utf-8') as file:
            content = file.read()
    except FileNotFoundError:
        print(f"文件未找到: {srt_file_path}")
        return
    except Exception as e:
        print(f"读取文件时出错: {e}")
        return

    # 匹配每个字幕块（从FrameCnt开始）
    block_pattern = re.compile(
        r'FrameCnt:.*?\[latitude:\s*([-+]?\d*\.\d+)\]\s*\[longitude:\s*([-+]?\d*\.\d+)\]'
        r'\s*\[rel_alt:\s*([-+]?\d*\.\d+).*?\]'
        r'.*?\[gb_yaw:\s*([-+]?\d*\.\d+)\s*gb_pitch:\s*([-+]?\d*\.\d+)\s*gb_roll:\s*([-+]?\d*\.\d+)\]',
        re.DOTALL
    )

    matches = block_pattern.findall(content)

    if not matches:
        print("未找到任何匹配的经纬度和姿态信息。")
        return

    # 30FPS时间戳递增
    timestamp = 0.0
    time_increment = 1.0 / 30.0  # 30fps

    tum_data = []
    source_srs = osr.SpatialReference()
    source_srs.ImportFromEPSG(4326)
    target_srs = osr.SpatialReference()
    target_srs.ImportFromEPSG(32650)
    coord_transform = osr.CoordinateTransformation(source_srs, target_srs)
    for lat, lon, rel_alt, gb_yaw, gb_pitch, gb_roll in matches:
        # 位置直接用经纬度和相对高度
        tx, ty, tz = float(lon), float(lat), float(rel_alt)
        tx, ty, _ = coord_transform.TransformPoint(ty, tx)

        # 转四元数
        qx, qy, qz, qw = euler_to_quaternion(float(gb_yaw), float(gb_pitch), float(gb_roll))

        line = f"{timestamp:.6f} {tx} {ty} {tz} {qx} {qy} {qz} {qw}"
        tum_data.append(line)
        timestamp += time_increment

    # 写入输出文件
    try:
        with open(output_file_path, 'w', encoding='utf-8') as out_file:
            out_file.write("\n".join(tum_data))
        print(f"成功提取 {len(tum_data)} 条数据，保存在 {output_file_path}")
    except Exception as e:
        print(f"写入文件时出错: {e}")

if __name__ == "__main__":
    input_srt = '/home/lty/datasets_my/DJI/m300/DJI_0110_6_W.SRT'      # 替换为你的SRT路径
    output_tum = '/home/lty/datasets_my/DJI/m300/DJI_0110_6_W_tum.txt'  # 输出TUM文件路径

    extract_tum_with_quaternion(input_srt, output_tum)
