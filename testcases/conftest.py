

import pytest
import requests

from common.logging import logger
from common.read_file import clear_yaml


@pytest.fixture(scope="module", autouse=True)
def connection_mysql():
    logger.debug("---------------测试开始--------------" )
    clear_yaml(r'D:\Django\demo\common\extract.yaml')
    yield
    logger.debug("------------结束测试-----------")

def pytest_collection_modifyitems(items):
    """
    测试用例收集完成时，将收集到的item的name和nodeid的中文显示在控制台上
    :return:
    """
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        print(item.nodeid)
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")

