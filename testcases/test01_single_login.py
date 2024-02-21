import logging

import allure
import pytest
from common.RestClient import HttpClient
from common.logging import  logger
from common.read_file import get_pwd_md5, read_yaml, write_yaml


# 单接口测试用户登录

class TestUserLogin:

    @allure.feature("用户登录")
    @pytest.mark.parametrize("login_data", read_yaml('./data/login.yaml'), ids=["输入正确账号、密码，登录成功",
                                                                                "账号为空，密码正确，登录失败",
                                                                                "账号正确，密码为空，登录失败",
                                                                                ])
    def test_user_login(self, login_data):
        logger.info("------开始执行用例-------")
        url = login_data["request"]["url"]
        print(login_data["request"]["json"]["password"])
        login_data["request"]["json"]["password"] = get_pwd_md5(login_data["request"]["json"]["password"])
        json = login_data["request"]["json"]
        res = HttpClient().send_request(method="post", url=url, json=json)
        assert res.json()["code"] == login_data["validate"]["code"]
        assert res.json()["message"] == login_data["validate"]["message"]
        logger.info(login_data)
        logger.info("期望结果：【{}】，实际结果：【{}】" .format(login_data["validate"]["message"],res.json()["message"]))
        logger.info("-----结束用例-----")





    # @allure.feature("用户登录")
    # @allure.title("错误的账号登录")
    # @pytest.mark.parametrize("login_data", read_yaml('./data/login.yaml')["test_email_error"])
    # def test_email_error(self, login_data):
    #     url = login_data["request"]["url"]
    #     login_data["request"]["json"]["password"] = get_pwd_md5(login_data["request"]["json"]["password"])
    #     json = login_data["request"]["json"]
    #     res = HttpClient().send_request(method="post", url=url, json=json)
    #     assert res.json()["code"] == login_data["validate"]["code"]
    #     assert res.json()["message"] == login_data["validate"]["message"]
    #
    # @allure.feature("用户登录")
    # @allure.title("错误的密码登录")
    # @pytest.mark.parametrize("login_data", read_yaml('./data/login.yaml')["test_password_error"])
    # def test_password_error(self, login_data):
    #     url = login_data["request"]["url"]
    #     login_data["request"]["json"]["password"] = get_pwd_md5(login_data["request"]["json"]["password"])
    #     json = login_data["request"]["json"]
    #     res = HttpClient().send_request(method="post", url=url, json=json)
    #     assert res.json()["code"] == login_data["validate"]["code"]
    #     assert res.json()["message"] == login_data["validate"]["message"]
