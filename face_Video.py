# coding:utf-8
# 真人人脸识别实时监测
# 从摄像头的视频图像中，获取图像

# Step 1. 导入开发框架
import cv2

# Step 2. 打开摄像头
captuer = cv2.VideoCapture(0)
# Step 4. 创建一个窗口
cv2.namedWindow(u"camera")
# Step 5. 实时检查摄像头
while  True :
    # 5.1 读取摄像头图片
    ret , frame = captuer.read()
    # 5.2 将图片转换为灰色图
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # 5.2 显示图片
    #img = cv2.imread('test.jpg')
    #cv2.imshow(u"photo", img)
    cv2.imshow(u"photo", frame)
    # 5.3 暂停窗口
    if cv2.waitKeyEx(5) & 0xFF == ord("q") :
        break

# Step 6. 释放资源
captuer.release()
# Step 7. 关闭窗口
cv2.destroyAllWindows()





