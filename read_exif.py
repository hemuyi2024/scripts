import subprocess
import json

def get_dji_xmp_data(filename):
    """
    读取 DJI 无人机照片的 XMP 元数据。

    参数：
    - filename: 图像文件的路径

    返回值：
    - xmp_data: 包含所需 XMP 信息的字典
    """
    # 定义需要提取的 XMP 标签
    tags = [
        '-j',
        '-XMP:Model',
        '-XMP:AbsoluteAltitude',
        '-XMP:RelativeAltitude',
        '-XMP:GpsLatitude',
        '-XMP:GpsLongitude',
        '-XMP:GimbalRollDegree',
        '-XMP:GimbalYawDegree',
        '-XMP:GimbalPitchDegree',
        filename
    ]

    # 调用 exiftool
    process = subprocess.run(['exiftool'] + tags, capture_output=True, text=True)
    if process.returncode != 0:
        print(f"Error: {process.stderr}")
        return None

    # 解析 JSON 输出
    output = process.stdout
    metadata = json.loads(output)
    return metadata[0] if metadata else None

# 示例使用
if __name__ == "__main__":
    file_name = "/home/lty/test/match_playground/seu_uav/DJI_0218.JPG"  # 替换为您的图像路径
    xmp_data = get_dji_xmp_data(file_name)
    print(xmp_data)

    if xmp_data:
        # 打印所需的 XMP 信息
        print("相机型号:", xmp_data.get('Xmp:Model'))
        print("绝对高度:", xmp_data.get('XMP:AbsoluteAltitude'))
        print("相对高度:", xmp_data.get('XMP:RelativeAltitude'))
        print("纬度:", xmp_data.get('XMP:GpsLatitude'))
        print("经度:", xmp_data.get('XMP:GpsLongitude'))
        print("Gimbal Roll Degree:", xmp_data.get('XMP:GimbalRollDegree'))
        print("Gimbal Yaw Degree:", xmp_data.get('XMP:GimbalYawDegree'))
        print("Gimbal Pitch Degree:", xmp_data.get('XMP:GimbalPitchDegree'))
    else:
        print("无法读取 DJI XMP 数据。")
