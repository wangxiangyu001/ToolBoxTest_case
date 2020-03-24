# coding:utf-8 #设置编码格式
import datetime
import time

import pytest

from toolBoxCase.ToolBoxOrientationUtil import appiumOrientation
from toolBoxCase.sendEmail import sendEmail


def test_main():
    appiumOrientation()
    assert appiumOrientation() == True ,'自动旋转开关为关'

if __name__ == '__main__':
    # now = datetime.datetime.now().strftime('%F-%T')
    # pytest.main(['--html=./report%s.html' % now])
    pytest.main(['--html=./report.html'])
    sendEmail()