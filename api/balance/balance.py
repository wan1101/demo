from common.RestClient import HttpClient
from common.read_file import read_yaml


class BalanceAPI:
    # 初始化
    def __init__(self):
        # 指定url基本信息
        # self.balance_list_url = config.BASE_URL+"/api/v1/balance"
        self.token = read_yaml("./common/extract.yaml")["token"]

    def get_balance_list(self):
        """
        获取列表
        :return:
        """
        url = "/api/v1/balance/list?page_num=1&page_size=100"
        headers = {
            "x-auth-token": self.token
        }
        # return requests.get(url=self.balance_list_url + "/list?page_num=1&page_size=100", headers=headers)
        return HttpClient().send_request(method="get", url=url, headers=headers)

    def balance_create(self, currency, name):
        """
         创建资金账户
        :param currency:币种
        :param name: 账户昵称
        :return:
        """
        url = "/api/v1/balance/create"
        headers = {
            "x-auth-token": self.token
        }
        json_data = {
            "currency": currency,
            "name": name
        }
        return HttpClient().send_request(method="post", url=url, headers=headers, json=json_data)

    def balance_retrieve(self, currency):
        """
        账户详情
        :return:
        """
        url = f"/api/v1/balance/retrieve?currency={currency}"
        headers = {
            "x-auth-token": self.token
        }
        return HttpClient().send_request(method="get", url=url, headers=headers)

    def transaction_list(self, currency):
        """
        账户详情列表
        :param currency:
        :return:
        """
        url = f"/api/v1/transaction/list?page_num=1&page_size=10&trans_currency={currency}&date_type=create_time"
        headers = {
            "x-auth-token": self.token
        }
        return HttpClient().send_request(method="get", url=url, headers=headers)
