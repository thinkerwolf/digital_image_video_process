import cv2
import matplotlib.pyplot as plt

# 读取图像
image = cv2.imread("images/example.jpg")

# 转为灰度
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 高斯模糊
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# 边缘检测
edges = cv2.Canny(blur, 50, 150)

# 显示结果
plt.figure(figsize=(10, 7))
plt.subplot(131), plt.imshow(gray, cmap="gray"), plt.title("Gray Image")
plt.subplot(132), plt.imshow(blur, cmap="gray"), plt.title("Blur Image")
plt.subplot(133), plt.imshow(edges, cmap="gray"), plt.title("Edges")
plt.show()
