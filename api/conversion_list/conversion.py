import requests

import config


#货币兑换
class ConversionAPI:
    # 初始化

    def __init__(self):
        # 指定url基本信息
        self.Conversion_create_time_url = config.BASE_URL + "/api/v1/conversion/list?page_num=1&page_size=10&date_type" \
                                                    "=create_time "

        self.Conversion_settle_time_url = config.BASE_URL + "/api/v1/conversion/list?page_num=1&page_size=10&date_type" \
                                                   "=settle_time"

    # 通过创建时间查看：货币兑换列表
    def get_conversion_clist(self, token):
        """
        通过创建时间查看：货币兑换列表
        :param token: 用户登录token
        :return:
        """

        headers = {
            "x-auth-token": token
        }
        return requests.get(url=self.Conversion_create_time_url, headers=headers)

    # 通过结算时间查看：货币兑换列表
    def get_conversion_slist(self, token):
        """
        通过结算时间查看：货币兑换列表
        :param token: 用户登录token
        :return:
        """
        headers = {
            "x-auth-token": token
        }
        return requests.get(url=self.Conversion_settle_time_url, headers=headers)

