import cv2

def rotate_image_180(image_path, output_path):
    # 读取图片
    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: Cannot read image from {image_path}")
        return

    # 旋转180度
    rotated_image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)

    # 保存旋转后的图片
    cv2.imwrite(output_path, rotated_image)
    print(f"Rotated image saved to {output_path}")

if __name__ == "__main__":
    # 输入图片路径和输出图片路径
    image_path = "/home/lty/test/match_playground/seu_uav/DJI_20250103123652_0002_W.JPG"  # 请修改为你的图片路径
    output_path = "/home/lty/test/match_playground/seu_uav/DJI_20250103123652_0002_W_rotate.JPG"  # 修改为你想保存的路径
    rotate_image_180(image_path, output_path)