import os
import time

import pytest

from common.read_file import read_yaml

if __name__ == "__main__":
    # login_data = read_yaml('./data/login.yaml')
    # print(login_data['test_login_success'])
    pytest.main()
    time.sleep(3)
    os.system("allure generate ./report/temps -o ./report/html --clean")

