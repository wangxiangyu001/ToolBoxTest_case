import os
import time

import pytest

from toolBoxCase.ToolBoxOrientationUtil import changeDisplayUp, checkDisplay, checkDisplayUpL, checkDisplayUpH


def test_main():
    # 先判断是横屏还是竖屏 再进行下面的操作
    if checkDisplay() == '0':
        # 判断为横屏设备
        changeDisplayUp()
        time.sleep(2)
        checkDisplayUpH()
        assert checkDisplayUpH() == True ,'屏幕向上旋转失败'
    else:
        # 非横屏设备
        changeDisplayUp()
        time.sleep(2)
        checkDisplayUpL()
        assert checkDisplayUpL() == True,'屏幕向上旋转失败'

if __name__ == '__main__':
    pytest.main(['--html=./report.html'])