import HTMLTestRunner
import time
import unittest

cases_dir = r'E:\auto\test_case\toolBoxCase'
def createsuite1():
    global test_case
    testunit = unittest.TestSuite()
    # 查找testList下的测试用例并加载
    discover = unittest.defaultTestLoader.discover(cases_dir, pattern='test_*.py', top_level_dir= None)
    print(cases_dir)
    print(discover)
    for test_suite in discover:
        print(test_suite)
        for test_case in test_suite:
            print(test_case)
            testunit.addTests(test_case)
            print(testunit)
    # testunit.addTest(discover)
    return testunit

if __name__ == '__main__':

    now = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime())
    # 测试报告存放路径 生成测试报告名称
    filename = "E:\\auto\\test_case\\report\\" + now + "_result.html"
    fp = open(filename, 'wb')

    runner = HTMLTestRunner.HTMLTestRunner(
        stream = fp,
        title = u'ToolBox自动化测试报告',
        description = u'用例执行情况：')
    runner.run(createsuite1())
    fp.close()

