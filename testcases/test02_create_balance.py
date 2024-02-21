import allure
import pytest
from api.balance.balance import BalanceAPI
from api.user.login import UserAPI
from common.read_file import read_yaml


class TestCreateBalance:
    @allure.title("添加新币种账户")
    @allure.description("用户登录——查看列表——添加币种")
    @pytest.mark.parametrize("testdata", read_yaml('./data/single_create_balance.yml'))
    def test_login_success(self, testdata):
        with allure.step("1.用户登录"):  # 在页面添加步骤
            UserAPI().get_login_token(testdata["email"], testdata["password"])
        with allure.step("2.查看账户资金列表"):
            BalanceAPI().get_balance_list()
        with allure.step("3.添加新币种账户"):
            res = BalanceAPI().balance_create(testdata["currency"], testdata["name"])
            assert res.json()["message"] == "The currency account has been added"

    #     url ="/api/v1/auth/signin"
    #
    #     login_data = {
    #         "email": testdata["email"],
    #         "password": get_pwd_md5(testdata["password"])
    #     }
    #     login_res = HttpClient().send_request(method="post", url=url, json=login_data)
    #     write_yaml({"token": "Bearer" + " " + login_res.json()['data']['access_token']}, './common/extract.yaml')
    #     assert login_res.json()["code"] == 200
    #
    #     url = "/api/v1/balance/list?page_num=1&page_size=100"
    #     headers = {
    #         "X-Auth-Token": read_yaml("./common/extract.yaml")["token"]
    #     }
    #     list_res = HttpClient().send_request(method="get", url=url, headers=headers)
    #     print(list_res.json())
    #
    # def test_balance_list(self):
    #     """
    #     用户登录获取token
    #     :return:
    #     """
    #     url = "/api/v1/balance/list?page_num=1&page_size=100"
    #     headers={
    #        "X-Auth-Token": read_yaml("./common/extract.yaml")["token"]
    #     }
    #     res = HttpClient().send_request(method="get", url=url, headers=headers)
    #     print(res.json())
    #     # assert res.json()["message"] == "Success"
    #
    # def test_balance_create(self):
    #     token = read_yaml("./common/extract.yaml")["token"]
    #     url="/api/v1/balance/create"
    #     header = {
    #         "X-Auth-Token": token,
    #         "Content-Type": "application/json"
    #     }
    #     json_data = {
    #         "currency": "NZD",
    #         "name": "ncui"
    #     }
    #     res = HttpClient().send_request(method="post", url=url, headers=header,json=json_data)
    #     print(res.json()["message"])


if __name__ == '__main__':
    pytest.main(["-vs"])
