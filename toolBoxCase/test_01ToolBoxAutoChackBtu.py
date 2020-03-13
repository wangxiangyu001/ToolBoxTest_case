# coding:utf-8 #设置编码格式
import pytest

from toolBoxCase.ToolBoxOrientationUtil import appiumOrientation


def test_main():
    appiumOrientation()
    assert appiumOrientation() == True ,'自动旋转开关为关'

if __name__ == '__main__':
    pytest.main(['--html=./report.html'])