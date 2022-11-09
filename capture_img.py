# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 10:50:30 2022

@TwinkelStar: 李星辰
@Email: xingchenziyi@163.com   
 
# ----------------------------------------------
#
#             双目视觉数据集制作
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
init_params.camera_fps = 30
runtime = sl.RuntimeParameters()
# 打开相机
err = zed.open(init_params)
if err != sl.ERROR_CODE.SUCCESS:
    exit(-1)

#创建mat类
image = sl.Mat()
while 1:
    #时间戳同步
    if zed.grab(runtime) == sl.ERROR_CODE.SUCCESS:
        #获取图像数据 可选择左右视图
        zed.retrieve_image(image, sl.VIEW.LEFT_UNRECTIFIED )
        cv.imshow("ZED", image.get_data())
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
cv.destroyAllWindows()
zed.disable_recording()
zed.close()