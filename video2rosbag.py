import cv2
import rospy
import rosbag
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

def mp4_to_rosbag(mp4_file, rosbag_file):
    # 初始化ROS节点
    rospy.init_node('mp4_to_rosbag_converter', anonymous=True)
    # 创建CvBridge对象，用于在OpenCV图像和ROS图像消息之间进行转换
    bridge = CvBridge()
    # 打开MP4视频文件
    cap = cv2.VideoCapture(mp4_file)
    # 创建一个新的rosbag文件
    bag = rosbag.Bag(rosbag_file, 'w')

    try:
        frame_id = 0
        while cap.isOpened():
            # 读取视频的下一帧
            ret, frame = cap.read()
            if not ret:
                break
            # 将OpenCV图像转换为ROS图像消息
            img_msg = bridge.cv2_to_imgmsg(frame, encoding="bgr8")
            img_msg.header.frame_id = str(frame_id)
            img_msg.header.stamp = rospy.Time.now()
            # 将图像消息写入rosbag文件
            bag.write('/camera/image_raw', img_msg, img_msg.header.stamp)
            frame_id += 1
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # 释放视频捕获对象
        cap.release()
        # 关闭rosbag文件
        bag.close()

if __name__ == "__main__":
    mp4_file = "your_video.mp4"  # 替换为实际的MP4视频文件路径
    rosbag_file = "output.bag"  # 替换为实际的rosbag文件路径
    mp4_to_rosbag(mp4_file, rosbag_file)