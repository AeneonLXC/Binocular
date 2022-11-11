# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 10:50:30 2022

@TwinkelStar: 李星辰
@Email: xingchenziyi@163.com   
 
# ----------------------------------------------
#
#              双目视觉数据集制作
#                  采集模块
#                 capture_img
#
#          LAST_UPDATE: Mon Nov  7 10:50:30 2022
#
# ----------------------------------------------

"""
import pyzed.sl as sl
import cv2 as cv
import time
zed = sl.Camera()
# 双目相机的基础配置
init_params = sl.InitParameters() #相机初始化
#相机采集模式 HD2K HD1080 HD720 VGA 
init_params.camera_resolution = sl.RESOLUTION.VGA  
#相机帧率设置 分辨率越高帧率越低
init_params.camera_fps = 30
#时间戳同步
runtime = sl.RuntimeParameters()
# 打开相机
err = zed.open(init_params)

#基础模块配置参数
video_setting = {
    "min": 1,
    "max": 8,
}
if err != sl.ERROR_CODE.SUCCESS:
    exit(-1)


def create_trackbars():
    """
    创建滑块控制函数
    """
    def nothing(x):
        """Nothing
        """
        pass
    #   灰度二值化滑块var值
    cv.namedWindow("ZED", cv.WINDOW_AUTOSIZE)
    cv.createTrackbar("BRIGHTNESS", 
                       "ZED", 
                       video_setting["min"], 
                       video_setting["max"], 
                       nothing)
    cv.createTrackbar("CONTRAST ", 
                       "ZED", 
                       video_setting["min"], 
                       video_setting["max"], 
                       nothing)
    cv.createTrackbar("SATURATION", 
                       "ZED", 
                       video_setting["min"], 
                       video_setting["max"], 
                       nothing)
    cv.createTrackbar("SHARPNESS", 
                       "ZED", 
                       video_setting["min"], 
                       video_setting["max"], 
                       nothing)
#创建mat类
image = sl.Mat()
create_trackbars()

while 1:
    #时间戳同步

    if zed.grab(runtime) == sl.ERROR_CODE.SUCCESS:
        #获取图像数据 可选择左右视图 LEFT or RIGHT
        value = cv.getTrackbarPos("BRIGHTNESS", "ZED")
        zed.set_camera_settings(sl.VIDEO_SETTINGS.BRIGHTNESS, value)
        zed.set_camera_settings(sl.VIDEO_SETTINGS.CONTRAST, value)
        zed.set_camera_settings(sl.VIDEO_SETTINGS.SATURATION, value)
        zed.set_camera_settings(sl.VIDEO_SETTINGS.SHARPNESS, value)
        zed.retrieve_image(image, sl.VIEW.SIDE_BY_SIDE)
        cv.imshow("ZED", image.get_data())
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
cv.destroyAllWindows()
zed.disable_recording()
zed.close()