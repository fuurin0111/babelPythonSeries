import cv2
import numpy as np

# 画像のサイズを指定
height, width = 1080,1920

# 0から255までのランダムな数値で満たされた3チャンネルの画像を作成
random_img = np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)\

# # 画像を表示
# cv2.imshow('Random Image', random_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 画像を保存
cv2.imwrite('random_image.png', random_img)
