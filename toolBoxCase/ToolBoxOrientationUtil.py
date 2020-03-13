import os

from toolBoxCase.ConfigTool import  toolConnectOrientationAppium


# 数据库中各个方向代表的值
# 竖屏：
# 正常方向（默认） '1'
# 向上旋转 '9'
# 向右旋转 '8'
# 向左旋转 '0'
# 横屏
# 正常方向（默认）‘0’
# 向上旋转 '8'
# 向右旋转 '1'
# 向左旋转 '9'


# 获取默认方向，用来判断是横屏设备还是竖屏设备
def checkDisplay():
    checkDisplayOrientation = os.popen('adb shell settings get global Sunmi_ORIENTATION').read().replace('\n', '')
    if checkDisplayOrientation == '0':
        return checkDisplayOrientation
    else:
        return checkDisplayOrientation


# 检查自动旋转开关默认状态
def appiumOrientation():
    toolConnectOrientationAppium.connectdrvier.implicitly_wait(20)
    # 获取开关状态
    statText = toolConnectOrientationAppium.connectdrvier.find_element_by_id('android:id/switch_widget').text
    toolConnectOrientationAppium.connectdrvier.implicitly_wait(20)
    # 判断状态
    if statText == '开启':
        print('默认为开')
        return True
    else:
        return False


# 获取数据库中当前屏幕显示方向的值
def checkDisplayStuat():
    stuatOrientation = os.popen('adb shell settings get global Sunmi_ORIENTATION ').read().replace('\n', '')
    return stuatOrientation


# 更改当前屏幕显示方向为向上
def changeDisplayUp():
    toolConnectOrientationAppium.connectdrvier.implicitly_wait(20)
    statText = toolConnectOrientationAppium.connectdrvier.find_element_by_id('android:id/switch_widget').text
    if statText == '开启':
        toolConnectOrientationAppium.connectdrvier.find_element_by_id('android:id/switch_widget').click()
    toolConnectOrientationAppium.connectdrvier.implicitly_wait(20)
    toolConnectOrientationAppium.connectdrvier.find_element_by_id('com.sunmi.toolbox:id/ck_top_sel').click()

# 检查当前是否为向上显示
# 竖屏
# 正常方向（默认） '1'
# 向上旋转 '9'
# 横屏
# 正常方向（默认）‘0’
# 向上旋转 '8'

# 竖屏
def checkDisplayUpL():
    if checkDisplayStuat() == '9':
        print("屏幕已向上旋转")
        return True
    else:
        return False
# 横屏
def checkDisplayUpH():
    if checkDisplayStuat() == '8':
        print("屏幕已向上旋转")
        return True
    else:
        return False

# 更改当前显示方向为向右
def changeDisplayRight():
    toolConnectOrientationAppium.connectdrvier.implicitly_wait(20)
    statText = toolConnectOrientationAppium.connectdrvier.find_element_by_id('android:id/switch_widget').text
    # 获取当前自动旋转开关状态，如果为开，则关闭
    if statText == '开启':
        toolConnectOrientationAppium.connectdrvier.find_element_by_id('android:id/switch_widget').click()

    toolConnectOrientationAppium.connectdrvier.implicitly_wait(20)
    toolConnectOrientationAppium.connectdrvier.find_element_by_id('com.sunmi.toolbox:id/ck_right_sel').click()

# 检查当前是否为向右显示
# 竖屏
# 正常方向（默认） '1'
# 向右旋转 '8'
# 横屏
# 正常方向（默认）‘0’
# 向右旋转 '1'

# 竖屏
def checkDisplayRightL():
    if checkDisplayStuat() == '8':
        print("屏幕已向右旋转")
        return True
    else:
        return False
# 横屏
def checkDisplayRightH():
    if checkDisplayStuat() == '1':
        print("屏幕已向右旋转")
        return True
    else:
        return False

# 更改当前显示方向为向左
def changeDisplayLeft():
    toolConnectOrientationAppium.connectdrvier.implicitly_wait(20)
    statText = toolConnectOrientationAppium.connectdrvier.find_element_by_id('android:id/switch_widget').text
    # 获取当前自动旋转开关状态，如果为开，则关闭
    if statText == '开启':
        toolConnectOrientationAppium.connectdrvier.find_element_by_id('android:id/switch_widget').click()

    toolConnectOrientationAppium.connectdrvier.implicitly_wait(20)
    toolConnectOrientationAppium.connectdrvier.find_element_by_id('com.sunmi.toolbox:id/ck_left_sel').click()

# 检查当前方向是否为向左
# 竖屏
# 正常方向（默认） '1'
# 向左旋转 '0'
# 横屏
# 正常方向（默认）‘0’
# 向左旋转 '9'
# 竖屏
def checkDisplayLeftL():
    if checkDisplayStuat() == '0':
        print("屏幕已向左显示")
        return  True
    else:
        return False
# 横屏
def checkDisplayLeftH():
    if checkDisplayStuat() == '9':
        print("屏幕已向左显示")
        return  True
    else:
        return False

# 更改当前显示方向为默认的向下方向
def changeDisplayDefault():
    # toolConnectappium.connectdrvier.implicitly_wait(20)
    statText = toolConnectOrientationAppium.connectdrvier.find_element_by_id('android:id/switch_widget').text
    # 获取当前自动旋转开关
    # 状态，如果为开，则关闭
    if statText == '开启':
        toolConnectOrientationAppium.connectdrvier.find_element_by_id('android:id/switch_widget').click()
    # toolConnectappium.connectdrvier.implicitly_wait(20)
    if  checkDisplay() == '0':
        toolConnectOrientationAppium.connectdrvier.find_element_by_id('com.sunmi.toolbox:id/ck_right_sel').click()
    elif checkDisplay() == '1':
        toolConnectOrientationAppium.connectdrvier.find_element_by_id('com.sunmi.toolbox:id/ck_down_sel').click()
    elif checkDisplay() == '8':
        toolConnectOrientationAppium.connectdrvier.find_element_by_id('com.sunmi.toolbox:id/ck_left_sel').click()
    else:
        toolConnectOrientationAppium.connectdrvier.find_element_by_id('com.sunmi.toolbox:id/ck_top_sel').click()


# 检查当前方向是否为默认方向
# 竖屏
# 正常方向（默认） '1'
# 横屏
# 正常方向（默认）‘0’
# 竖屏
def checkDisplayDefaultL():
    if checkDisplayStuat() == '1':
        print("屏幕已调回默认方向")
        return  True
    else:
        return False
# 横屏
def checkDisplayDefaultH():
    if checkDisplayStuat() == '0':
        print("屏幕已调回默认方向")
        return  True
    else:
        return False