

from baiduapi import BaiDuAPI
import cv2




if __name__ == '__main__':  
    print('---------正在检测-----------')

    baiduapi = BaiDuAPI('human_detection.ini')

    # Step 2. 打开摄像头
    captuer = cv2.VideoCapture(0)
    #参数设置
    captuer.set(3,480)#视频每一帧的宽
    captuer.set(4,320)#视频每一帧的高
    # Step 4. 创建一个窗口
    cv2.namedWindow(u"摄像头")
    # Step 5. 实时检查摄像头
    while  True :
        # 5.1 读取摄像头图片
        ret , frame = captuer.read()
        #s = base64_data.decode()
        # 5.2 将图片转换为灰色图
        #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # 5.2 显示图片
        if(ret) : 
            baiduapi.file_main(frame)
            #baiduapi.file_main('test.jpg')
            #cv2.imshow(u"显示图片", frame)
        # 5.3 暂停窗口
        if cv2.waitKeyEx(5) & 0xFF == ord("q") :
            break

    # Step 6. 释放资源
    captuer.release()
    # Step 7. 关闭窗口
    cv2.destroyAllWindows()

    
    print('---------检测完成-----------')

