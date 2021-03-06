import datetime
import time

import pytest

from toolBoxCase.ToolBoxOrientationUtil import checkDisplay, changeDisplayLeft, checkDisplayLeftH, \
    changeDisplayDefaultH, checkDisplayLeftL, changeDisplayDefaultL
from toolBoxCase.sendEmail import sendEmail


def test_main():
    # 先判断是横屏还是竖屏 再进行下面的操作
    if checkDisplay() == '0':
        # 判断为横屏设备
        changeDisplayLeft()
        time.sleep(2)
        checkDisplayLeftH()
        assert checkDisplayLeftH() == True, '屏幕向右旋转失败'
        changeDisplayDefaultH()
    else:
        # 非横屏设备
        changeDisplayLeft()
        time.sleep(2)
        checkDisplayLeftL()
        assert checkDisplayLeftL() == True, '屏幕向右旋转失败'
        changeDisplayDefaultL()
    print('已恢复默认')


if __name__ == '__main__':
    # now = datetime.datetime.now().strftime('%F%T')
    # pytest.main(['--html=./report%s.html' % now])
    # sendEmail()
    pytest.main(['--html=./report.html'])
    sendEmail()