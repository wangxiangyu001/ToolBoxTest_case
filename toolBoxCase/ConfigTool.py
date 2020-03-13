import os

from appium import webdriver
import subprocess

# com.sunmi.toolbox/.key.CustomKeyActivity 按键自定义页面
# com.sunmi.toolbox/.deviceinfo.OtherInfoActivity  其他信页面
# com.sunmi.toolbox/.networkmanager.NetworkManagerActivity 智能网络管理页面
# com.sunmi.toolbox/.orientation.OrientationActivity  屏幕旋转页面
# com.sunmi.toolbox/.timerswitch.TimerSwitchActivity 定时开关机页面
# com.sunmi.toolbox/.timerswitch.ShutdownActivity 定时关机弹窗
# com.sunmi.toolbox/.ntp.NtpActivity  时间服务器（自定义NTP）页面
# com.sunmi.toolbox/.applock.AuthLaunchLockedAppActivity 内存泄露检测页面
# om.sunmi.toolbox/.ptt.ui.PttActivity 对讲机
# com.sunmi.toolbox/.ethernet.EthernetActivity 有线网页面
# com.sunmi.toolbox/.key.CustomKeyActivity
# com.sunmi.toolbox/.orientation.OrientationActivity
# com.sunmi.toolbox/.laboratory.LabActivity  实验室页面
# com.sunmi.toolbox.key.KeySettingsActivity
# com.sunmi.toolbox.key.CustomKeyActivity
# 定义连接参数
platformName = 'Android'
# platformVersion = '7.1.2'
# deviceName = 'V220KJ0828017'
appPackage = 'com.sunmi.toolbox'
# 获取android版本
platformVersion = os.popen('adb shell getprop ro.build.version.release').read()
# 获取设备SN
deviceSN = os.popen('adb shell getprop ro.serialno').read()

class toolConnectOrientationAppium:
    appActivity = 'com.sunmi.toolbox.orientation.OrientationActivity'
    # 建立连接参数字典
    paramters = {'platformName':platformName,
                'platformVersion':platformVersion,
                'deviceName':deviceSN,
                'appPackage':appPackage,
                'appActivity':appActivity}

    connectdrvier = webdriver.Remote('http://127.0.0.1:4723/wd/hub', paramters)

    connectdrvier.implicitly_wait(20)
    # 获取当前窗口宽高
    height = connectdrvier.get_window_size()['height']
    width = connectdrvier.get_window_size()['width']


    def appiumConnect(self):
        commed = 'adb devices'
        pi = subprocess.Popen(commed, shell=True, stdout=subprocess.PIPE)
        print(pi.stdout.read())

    def brackAppiumConnect(self):
        toolConnectOrientationAppium.connectdrvier.quit()