import re

def extract_lat_lon_from_srt(srt_file_path, output_file_path):
    """
    从给定的SRT文件中提取所有经纬度信息，并保存到输出文件中。

    :param srt_file_path: 输入的SRT文件路径
    :param output_file_path: 输出的TXT文件路径
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

    # 定义一个正则表达式模式，以同时匹配纬度和经度
    pattern = re.compile(
        r'\[latitude:\s*([-+]?\d*\.\d+|\d+)\]\s*\[longitude:\s*([-+]?\d*\.\d+|\d+)\]',
        re.IGNORECASE
    )

    # 查找所有匹配的经纬度对
    matches = pattern.findall(content)

    if not matches:
        print("未找到任何经纬度信息。")
        return

    # 格式化经纬度对
    lat_lon_list = [f"{lon}, {lat}" for lat, lon in matches]

    try:
        with open(output_file_path, 'w', encoding='utf-8') as out_file:
            for lat_lon in lat_lon_list:
                out_file.write(lat_lon + '\n')
        print(f"成功提取 {len(lat_lon_list)} 条经纬度信息，保存在 {output_file_path}")
    except Exception as e:
        print(f"写入文件时出错: {e}")

if __name__ == "__main__":
    # 指定SRT文件的路径和输出文件的路径
    input_srt = '/home/lty/datasets_my/DJI/m300/DJI_0110_6_W.SRT'      # 替换为你的SRT文件路径
    output_txt = '/home/lty/datasets_my/DJI/m300/DJI_0110_6_W_gt.txt'    # 替换为你希望保存的TXT文件路径

    extract_lat_lon_from_srt(input_srt, output_txt)
