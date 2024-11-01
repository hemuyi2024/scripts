import subprocess
import json
import re

# 读取大疆无人机录制的视频文件路径
video_file = r"E:\data\DJI\2024-11-1\DJI_0027.MOV"

# 使用 ffmpeg 提取视频元数据
try:
    result = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "stream", "-of", "json", video_file],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    if result.returncode != 0:
        print(f"FFprobe 错误信息: {result.stderr}")
    else:
        metadata = json.loads(result.stdout)
        # 提取所有元数据
        streams = metadata.get("streams", [])
        for stream in streams:
            # 输出所有元数据信息
            print(json.dumps(stream, indent=4))
except FileNotFoundError:
    print("ffprobe 未找到，请确保已安装并配置在系统路径中。")
except json.JSONDecodeError:
    print("解析 JSON 时出现错误。")
