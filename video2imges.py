import cv2
import os

# 视频文件路径
videoFile = "C:\\Users\\hp\\Desktop\\DJI_0022.MOV"  # 修改为你的视频路径
outputFolder = "C:\\Users\\hp\\Desktop\\calibr" # 修改为输出图片的文件夹

# 创建输出文件夹
if not os.path.exists(outputFolder):
    os.makedirs(outputFolder)

# 打开视频文件
cap = cv2.VideoCapture(videoFile)
if not cap.isOpened():
    print(f"无法打开视频文件: {videoFile}")
    exit()

frameNumber = 0

# 提取视频帧并保存为图片
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # 保存每一帧为图像
    filename = os.path.join(outputFolder, f"frame_{frameNumber:05d}.png")
    cv2.imwrite(filename, frame)

    frameNumber += 1

cap.release()
print("视频帧提取完成。")
