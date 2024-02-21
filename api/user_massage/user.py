import requests


class UserAPI:
    # 初始化

    def __init__(self):
        # 指定url基本信息
        self.user_massage_url = "https://dashapi.uqpay.dev/api/v1/user/account"

    # 获取用户信息
    def get_user_massage(self,token):
        headers = {
            "x-auth-token": token
        }
        return requests.get(url=self.user_massage_url,headers=headers)


