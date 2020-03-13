import time

import pytest

from toolBoxCase.ToolBoxOrientationUtil import changeDisplayLeft, checkDisplay, checkDisplayLeftL, checkDisplayLeftH


def test_main():
    # 先判断是横屏还是竖屏 再进行下面的操作
    if checkDisplay() == '0':
        # 判断为横屏设备
        changeDisplayLeft()
        time.sleep(2)
        checkDisplayLeftH()
        assert checkDisplayLeftH() == True, '屏幕向右旋转失败'
    else:
        # 非横屏设备
        changeDisplayLeft()
        time.sleep(2)
        checkDisplayLeftL()
        assert checkDisplayLeftL() == True, '屏幕向右旋转失败'

if __name__ == '__main__':
    pytest.main(['--html=./report.html'])