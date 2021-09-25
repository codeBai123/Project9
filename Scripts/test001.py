import allure
import pytest

class Test_01:
    @allure.step(title="第一个测试")
    @pytest.allure.severity(allure.severity_level.BLOCKER)
    def test_01(self):
        allure.attach("111", "222")
        assert 1

    @allure.issue('http://www.163.com')
    @pytest.allure.testcase('http://www.baidu.com/test_02')
    @pytest.allure.severity(allure.severity_level.TRIVIAL)
    def test_02(self):
        allure.attach("333", "444")
        assert 1

