import configparser
from logging import log

from _pytest import logging

"""
    解析配置文件
"""


def conf_read(conf_path, section, option):
    conf = configparser.ConfigParser()
    conf.read(conf_path)
    value = conf.get(section, option)
    return value


if __name__ == '__main__':
    res = conf_read(r'./serves.ini', 'DEV', 'url')
    print(res)