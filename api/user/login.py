import config
from common.RestClient import HttpClient
from common.read_file import get_pwd_md5, write_yaml, read_yaml


class UserAPI:
    def __init__(self):
        self.token = read_yaml("./common/extract.yaml")["token"]



    def get_login_token(self,email,password):
        """
        用户登录
        :param email: 邮箱
        :param password: 密码
        :return:
                {
    "code": 200,
    "message": "Success",
    "data": {
        "email": "853467358@qq.com",
        "user_id": "bfb17a60-c68f-4c11-8f3e-9968a00f0692",
        "username": "sj ",
        "customer_id": "0732d4a4-a33f-463c-bae6-bdf285d6ca0e",
        "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6Ijg1MzQ2NzM1OEBxcS5jb20iLCJ1c2VybmFtZSI6InNqICIsInVzZXJfaWQiOiJiZmIxN2E2MC1jNjhmLTRjMTEtOGYzZS05OTY4YTAwZjA2OTIiLCJjdXN0b21lcl9pZCI6IjA3MzJkNGE0LWEzM2YtNDYzYy1iYWU2LWJkZjI4NWQ2Y2EwZSIsIm1hc3Rlcl9pZCI6IjAiLCJvbl9iZWhhbGZfaWQiOiIiLCJvbl9iZWhhbGZfbmFtZSI6IiIsImFjY291bnRfaWQiOiIwNzMyZDRhNC1hMzNmLTQ2M2MtYmFlNi1iZGYyODVkNmNhMGUiLCJkaXJlY3RfaWQiOiIwIiwiZXhwIjoxNzA4NTg2OTI2LCJpc3MiOiJ1cXBheSJ9.bfJXXUZijKknPxgA58N3_eZHbICq6Biuis3zn2iv4JI",
        "expire_time": 1708586926,
        "role": "owner",
        "refresh_token": "a32b59140229589dda374f93b4f9517e1f9c911f948811ab960a3863bf0d85cb",
        "refresh_token_expire_time": 1709105326,
        "short_customer_id": "B50095872",
        "customer_status": 2,
        "role_id": "00000000-0000-0000-0000-000000000001"
    }
}
        """
        url ="/api/v1/auth/signin"
        login_data = {
            "email": email,
            "password": get_pwd_md5(password)
        }
        res = HttpClient().send_request(method="post", url=url, json=login_data)
        write_yaml({"token": "Bearer" + " " + res.json()['data']['access_token']}, './common/extract.yaml')
        return res

    def user_customer(self):
        """
        用户信息
        :return:
                {
    "code": 200,
    "message": "Success",
    "data": {
        "master_id": "0",
        "customer_id": "0732d4a4-a33f-463c-bae6-bdf285d6ca0e",
        "user_id": "bfb17a60-c68f-4c11-8f3e-9968a00f0692",
        "short_customer_id": "B50095872",
        "account_id": "0732d4a4-a33f-463c-bae6-bdf285d6ca0e",
        "email": "853467358@qq.com",
        "username": "sj ",
        "customer_type": 2000,
        "entity_type": "company",
        "crypto_status": 0,
        "role_id": "00000000-0000-0000-0000-000000000001",
        "customer_status": 2,
        "verification_status": "pending",
        "account_type": "LPSP",
        "hidden_menus": [
            "cryptocurrency"
        ],
        "permission_list": [
            {
                "permission_name": "Payout",
                "permission_code": "payout",
                "has_action": 1,
                "select_all_actions": 1,
                "action": {
                    "allow_view": 1,
                    "allow_create": 1,
                    "allow_update": 1,
                    "allow_delete": 1
                }
            },
            {
                "permission_name": "Balances",
                "permission_code": "balances",
                "has_action": 1,
                "select_all_actions": 1,
                "action": {
                    "allow_view": 1,
                    "allow_create": 1,
                    "allow_update": 1,
                    "allow_delete": 1
                }
            },
            {
                "permission_name": "Conversion",
                "permission_code": "conversion",
                "has_action": 1,
                "select_all_actions": 1,
                "action": {
                    "allow_view": 1,
                    "allow_create": 1,
                    "allow_update": 1,
                    "allow_delete": 1
                }
            },
            {
                "permission_name": "Beneficiaries",
                "permission_code": "beneficiaries",
                "has_action": 1,
                "select_all_actions": 1,
                "action": {
                    "allow_view": 1,
                    "allow_create": 1,
                    "allow_update": 1,
                    "allow_delete": 1
                }
            },
            {
                "permission_name": "Transactions",
                "permission_code": "transactions",
                "has_action": 1,
                "select_all_actions": 1,
                "action": {
                    "allow_view": 1,
                    "allow_create": 1,
                    "allow_update": 1,
                    "allow_delete": 1
                }
            },
            {
                "permission_name": "Card",
                "permission_code": "card",
                "has_action": 0,
                "select_all_actions": 1,
                "permission_items": [
                    {
                        "permission_name": "Card List",
                        "permission_code": "card_list",
                        "has_action": 1,
                        "select_all_actions": 1,
                        "action": {
                            "allow_view": 1,
                            "allow_create": 1,
                            "allow_update": 1,
                            "allow_delete": 1
                        }
                    },
                    {
                        "permission_name": "Card Holder",
                        "permission_code": "card_holder",
                        "has_action": 1,
                        "select_all_actions": 1,
                        "action": {
                            "allow_view": 1,
                            "allow_create": 1,
                            "allow_update": 1,
                            "allow_delete": 1
                        }
                    },
                    {
                        "permission_name": "Card Transactions",
                        "permission_code": "card_transactions",
                        "has_action": 1,
                        "select_all_actions": 1,
                        "action": {
                            "allow_view": 1,
                            "allow_create": 1,
                            "allow_update": 1,
                            "allow_delete": 1
                        }
                    }
                ]
            },
            {
                "permission_name": "Reports",
                "permission_code": "reports",
                "has_action": 1,
                "select_all_actions": 1,
                "action": {
                    "allow_view": 1,
                    "allow_create": 1,
                    "allow_update": 1,
                    "allow_delete": 1
                }
            },
            {
                "permission_name": "Team management",
                "permission_code": "team_management",
                "has_action": 1,
                "select_all_actions": 1,
                "action": {
                    "allow_view": 1,
                    "allow_create": 1,
                    "allow_update": 1,
                    "allow_delete": 1
                }
            },
            {
                "permission_name": "Developer",
                "permission_code": "developer",
                "has_action": 1,
                "select_all_actions": 1,
                "action": {
                    "allow_view": 1,
                    "allow_create": 1,
                    "allow_update": 1,
                    "allow_delete": 1
                }
            }
        ],
        "app_list": [
            {
                "app_id": "",
                "app_code": "VA_ACCOUNT",
                "app_name": "Virtual Account",
                "app_type": 1000,
                "expire_time": 0,
                "app_status": 0,
                "onboarding_step": 0,
                "onboarding_steps_required": 3,
                "base_complete": false
            },
            {
                "app_id": "",
                "app_code": "AC_ACQUIRER",
                "app_name": "Acquirer",
                "app_type": 3000,
                "expire_time": 0,
                "app_status": 0,
                "onboarding_step": 0,
                "onboarding_steps_required": 4,
                "base_complete": false
            }
        ]
    }
}
        """
        url = "/api/v1/onboarding/entrance/user/customer"
        headers = {
            "x-auth-token":  self.token
        }

        return HttpClient().send_request(method="GET", url=url, headers=headers)


    def user_entrance_app_list(self):
        """
        applist
        :return:{
                "code": 200,
                "message": "Success",
                "data": {
                    "app_list": [
                        {
                            "app_id": "",
                            "app_code": "VA_ACCOUNT",
                            "app_name": "Virtual Account",
                            "app_type": 1000,
                            "expire_time": 0,
                            "app_status": 0,
                            "onboarding_step": 0,
                            "onboarding_steps_required": 3,
                            "base_complete": false
                        },
                        {
                            "app_id": "",
                            "app_code": "AC_ACQUIRER",
                            "app_name": "Acquirer",
                            "app_type": 3000,
                            "expire_time": 0,
                            "app_status": 0,
                            "onboarding_step": 0,
                            "onboarding_steps_required": 4,
                            "base_complete": false
                        }
                    ]
                }
            }
        """

        url = "/api/v1/onboarding/entrance/app/list"
        headers = {
            "x-auth-token":  self.token
        }

        return HttpClient().send_request(method="GET", url=url, headers=headers)


    def user_sign_out(self):
        """
        用户退出
        :return:{"code":200,"message":"Success"}
        """
        url = "/api/v1/onboarding/entrance/user/sign_out"
        headers = {
            "x-auth-token":  self.token
        }
        return HttpClient().send_request(method="GET", url=url, headers=headers)


