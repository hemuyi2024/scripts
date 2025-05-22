
import cv2

# 输入和输出图像的路径
input_path = '/home/lty/test/match_playground/seu_uav/00000_0110_11.png'      # 替换为您的输入图像路径
output_path = '/home/lty/test/match_playground/seu_uav/00000_0110_11(gray).png'    # 替换为您希望保存的输出图像路径

# 读取彩色图像
color_image = cv2.imread(input_path)

# 检查图像是否成功读取
if color_image is None:
    print(f"无法读取图像: {input_path}")
    exit()

# 将图像转换为灰度
grayscale_image = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)

# 保存灰度图像
cv2.imwrite(output_path, grayscale_image)

print(f"灰度图像已保存为: {output_path}")
