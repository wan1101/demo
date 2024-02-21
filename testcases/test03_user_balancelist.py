import pytest

from api.dispute_list.dispute import DisputeAPI
from api.user_massage.login import LoginAPI
from common.read_file import get_pwd_md5, write_yaml, read_yaml



# 用户登录——>查看资金账户列表

class TestUserMassage:

    # @pytest.mark.parametrize("cg,sb", read_yaml('../data/single_create_balance.yml'))
    def test_get_login(self):
        """
        用户登录获取token
        :return:
        """
        login_data = {
            "email": "1442685214@qq.com",
            "password": get_pwd_md5('Qaz!1234')
        }
        res = LoginAPI().get_login_token(login_data)
        print(res.json())
        assert res.json()['code'] == 200

        write_yaml({"token":"Bearer"+" "+res.json()['data']['access_token']}, '../common/extract.yaml')
        res = DisputeAPI().get_dispute_list(read_yaml('../common/extract.yaml')["token"])
        print(read_yaml('../common/extract.yaml')["token"])
        print(res.json())
        assert res.json()['code'] == 200
        assert res.json()['message'] == "Success"



