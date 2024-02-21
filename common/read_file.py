#  读取json文件
import json
import os

import yaml


# 读取json文件数据驱动参数使用
def read_jsonfile(json_file):
    login_data = []
    with open(json_file, "r", encoding="UTF-8") as f:
        json_data = json.load(f)
        for case_data in json_data:
            email = case_data.get("email")
            password = case_data.get("password")
            status_code = case_data.get("status_code")
            message = case_data.get("message")
            login_data.append((email, password, status_code, message))

    return login_data


# MD5加密
def get_pwd_md5(word):
    import hashlib
    md5 = hashlib.md5()
    md5.update(word.encode('utf-8'))
    password = md5.hexdigest()
    return password


# 写入：追加 参数关联使用
def write_yaml(data,path):
    with open( path, encoding="utf-8", mode="a+") as f:
        yaml.dump(data, stream=f, allow_unicode=True)


# 读取
def read_yaml(path):
    with open(path, encoding="utf-8", mode="r") as f:
        value = yaml.load(f, yaml.FullLoader)
        return value


# 清空
def clear_yaml(path):
    with open(path, encoding="utf-8", mode="w") as f:
        f.truncate()


