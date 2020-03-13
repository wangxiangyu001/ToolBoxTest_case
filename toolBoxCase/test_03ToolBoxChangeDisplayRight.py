import os
import time

import pytest

# from toolBoxCase.ConfigTool import toolConnectappium
from toolBoxCase.ToolBoxOrientationUtil import changeDisplayRight, checkDisplay, checkDisplayRightH, checkDisplayRightL


def test_main():
    # 先判断是横屏还是竖屏 再进行下面的操作
    if checkDisplay() == '0':
        # 判断为横屏设备
        changeDisplayRight()
        time.sleep(2)
        checkDisplayRightH()
        assert checkDisplayRightH() == True, '屏幕向右旋转失败'
    else:
        # 非横屏设备
        changeDisplayRight()
        time.sleep(2)
        checkDisplayRightL()
        assert checkDisplayRightL() == True, '屏幕向右旋转失败'


if __name__ == '__main__':
    pytest.main(['--html=./report.html'])