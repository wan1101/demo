from common.RestClient import HttpClient
from common.read_file import read_yaml


class BalanceAPI:
    # 初始化
    def __init__(self):
        # 指定url基本信息
        # self.balance_list_url = config.BASE_URL+"/api/v1/balance"
        self.token = read_yaml("./common/extract.yaml")["token"]

    #  获取列表
    def get_balance_list(self):
        url = "/api/v1/balance/list?page_num=1&page_size=100"
        headers = {
            "x-auth-token": self.token
        }
        # return requests.get(url=self.balance_list_url + "/list?page_num=1&page_size=100", headers=headers)
        return HttpClient().send_request(method="get", url=url, headers=headers)

    #  创建资金账户
    def create_balance(self, currency,name):
        """
        :param currency:币种
        :param name: 账户昵称
        :return:
        """
        url="/api/v1/balance/create"
        headers = {
            "x-auth-token": self.token
        }
        json_data = {
            "currency":currency,
            "name": name
        }
        # return requests.post(url=self.balance_list_url + "/create", headers=headers, params=json_data)
        return HttpClient().send_request(method="post", url=url, headers=headers,json=json_data)
