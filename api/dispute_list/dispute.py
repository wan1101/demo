import requests

# 合规案例
from config import BASE_URL


class DisputeAPI:
    # 初始化

    def __init__(self):
        # 指定url基本信息
        self.dispute_list_url = BASE_URL + "/api/v1/dispute/list?page_num=1&page_size=5"


    # 获取用户token
    def get_dispute_list(self, token):

        headers = {
            "x-auth-token": token
        }
        return requests.get(url=self.dispute_list_url, headers=headers)



