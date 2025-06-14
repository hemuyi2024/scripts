import cv2
import os
#video->images

if __name__ == '__main__':
    # 视频文件路径
    videoFile = '/media/lty/Data/data/DJI/2024-11-21-playground/720p/DJI_0170.MP4'  # 修改为你的视频路径
    outputFolder = '/home/lty/datasets_my/DJI/phantom4/11-21-playground/720p/DJI_0170' # 修改为输出图片的文件夹

    # 创建输出文件夹
    if not os.path.exists(outputFolder):
        os.makedirs(outputFolder)

    # 打开视频文件
    cap = cv2.VideoCapture(videoFile)
    if not cap.isOpened():
        print(f"无法打开视频文件: {videoFile}")
        exit()

    frameNumber = 0
    imgNumber = 0
    # 提取视频帧并保存为图片
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # 保存每n帧为图像
        if frameNumber %3 == 0:
            filename = os.path.join(outputFolder, f"{imgNumber:05d}.png")
            frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            cv2.imwrite(filename, frame_gray)
            print(f"saved image: {filename}")
            imgNumber += 1

        frameNumber += 1

    cap.release()
    print("视频帧提取完成。")
    print(f"总共提取了 {imgNumber} 张图片。")


# # 视频文件路径
# videoFile = '/home/lty/datasets_my/DJI/m300/DJI_0110_0006_W.MP4'  # 修改为你的视频路径
# outputFolder = '/home/lty/datasets_my/DJI/m300/seu_uav_0110_6' # 修改为输出图片的文件夹
#
# # 创建输出文件夹
# if not os.path.exists(outputFolder):
#     os.makedirs(outputFolder)
#
# # 打开视频文件
# cap = cv2.VideoCapture(videoFile)
# if not cap.isOpened():
#     print(f"无法打开视频文件: {videoFile}")
#     exit()
#
# frameNumber = 0
# imgNumber = 0
# # 提取视频帧并保存为图片
# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break
#
#     # 保存每n帧为图像
#     if frameNumber %1 == 0:
#         filename = os.path.join(outputFolder, f"{imgNumber:05d}.png")
#         frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#         cv2.imwrite(filename, frame_gray)
#         print(f"saved image: {filename}")
#         imgNumber += 1
#
#     frameNumber += 1
#
# cap.release()
# print("视频帧提取完成。")
# print(f"总共提取了 {imgNumber} 张图片。")
