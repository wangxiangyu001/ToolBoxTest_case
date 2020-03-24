import datetime
import time

import pytest

from toolBoxCase.ToolBoxOrientationUtil import checkDisplayDefaultL, checkDisplay, checkDisplayDefaultH, \
    changeDisplayDefaultL, changeDisplayDefaultH
from toolBoxCase.sendEmail import sendEmail


def test_main():
    # 先判断是横屏还是竖屏 再进行下面的操作
    if checkDisplay() == '0':
        # 判断为横屏设备
        changeDisplayDefaultH()
        time.sleep(2)
        checkDisplayDefaultH()
        assert checkDisplayDefaultH() == True, '屏幕调整为默认方向失败'
    else:
        # 非横屏设备
        changeDisplayDefaultL()
        time.sleep(2)
        checkDisplayDefaultL()
        assert checkDisplayDefaultL() == True, '屏幕调整为默认方向失败'

if __name__ == '__main__':
    # now = datetime.datetime.now().strftime('%F%T')
    # pytest.main(['--html=./report%s.html' % now])
    # sendEmail()
    pytest.main(['--html=./report.html'])
    sendEmail()