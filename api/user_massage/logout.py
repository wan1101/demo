import requests

import config


class LogoutAPI:
    # 初始化

    def __init__(self):
        # 指定url基本信息
        self.bash_url = config.BASE_URL +"/api/v1/user/sign_out"

    # 用户退出

    def get_user_logout(self,token):
        headers = {
            "x-auth-token": token
        }
        return requests.get(url=self.bash_url,headers=headers)
