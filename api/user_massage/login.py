import config
from common.RestClient import HttpClient
from common.read_file import get_pwd_md5, write_yaml


class LoginAPI:
    def __init__(self):
    #指定url基本信息
        self.bash_url = config.BASE_URL

    # 用户登录获取token
    def get_login_token(self,email,password):
        """
        用户登录
        :param email: 邮箱
        :param password: 密码
        :return: 请求结果
        """
        url ="/api/v1/auth/signin"
        login_data = {
            "email": email,
            "password": get_pwd_md5(password)
        }
        res = HttpClient().send_request(method="post", url=url, json=login_data)

        write_yaml({"token": "Bearer" + " " + res.json()['data']['access_token']}, './common/extract.yaml')
        return res




