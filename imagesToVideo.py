import cv2
import os

# images -> video

if __name__ == '__main__':
    # 图片文件夹路径
    imageFolder = '/home/lty/datasets_my/DJI/m300/seu_uav_0110_6(color)'  # 修改为你的图片文件夹路径
    outputVideo = '/home/lty/datasets_my/DJI/m300/seu_uav_0110_6(color).mp4'  # 修改为输出视频的路径

    # 获取图片列表
    images = [img for img in os.listdir(imageFolder) if img.endswith(".png")]
    images.sort()  # 按文件名排序

    if not images:
        print(f"文件夹中没有图片: {imageFolder}")
        exit()

    # 读取第一张图片以获取尺寸信息
    firstImagePath = os.path.join(imageFolder, images[0])
    frame = cv2.imread(firstImagePath)
    height, width, layers = frame.shape

    # 设置视频编码器和输出视频参数
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # 视频编码器
    fps = 30  # 帧率
    videoWriter = cv2.VideoWriter(outputVideo, fourcc, fps, (width, height))

    if not videoWriter.isOpened():
        print(f"无法创建视频文件: {outputVideo}")
        exit()

    # 将图片写入视频
    for image in images:
        imagePath = os.path.join(imageFolder, image)
        frame = cv2.imread(imagePath)
        videoWriter.write(frame)
        print(f"写入帧: {image}")

    videoWriter.release()
    print("视频合成完成。")
    print(f"视频已保存到: {outputVideo}")