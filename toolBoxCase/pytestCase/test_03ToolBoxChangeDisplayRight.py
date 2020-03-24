import datetime
import os
import time

import pytest

from toolBoxCase.ToolBoxOrientationUtil import checkDisplay, changeDisplayRight, checkDisplayRightH, \
    changeDisplayDefaultH, checkDisplayRightL, changeDisplayDefaultL
from toolBoxCase.sendEmail import sendEmail


def test_main():
    # 先判断是横屏还是竖屏 再进行下面的操作
    if checkDisplay() == '0':
        # 判断为横屏设备
        changeDisplayRight()
        time.sleep(2)
        checkDisplayRightH()
        assert checkDisplayRightH() == True, '屏幕向右旋转失败'
        changeDisplayDefaultH()
    else:
        # 非横屏设备
        changeDisplayRight()
        time.sleep(2)
        checkDisplayRightL()
        assert checkDisplayRightL() == True, '屏幕向右旋转失败'
        changeDisplayDefaultL()
    print('已恢复默认')


if __name__ == '__main__':
    # now = datetime.datetime.now().strftime('%F%T')
    # pytest.main(['--html=./report%s.html' % now])
    # sendEmail()
    pytest.main(['--html=./report.html'])
    sendEmail()