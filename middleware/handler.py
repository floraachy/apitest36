"""
======================================
Author: Flora.Chen
Time: 2021/3/11 21:53
~ _ ~ ~ _ ~ ~ _ ~ ~ _ ~ ~ _ ~ ~ _ ~ 
======================================
"""
import os, re
from conf.project_path import LOG_PATH, CONF_PATH, DATA_PATH
from common.handle_log import get_logger
from common.handle_yaml import HandleYaml
from common.handle_excel import HandleExcel
from common.handle_mysql import DBHandler
import pymysql


class MidDBHandler(DBHandler):
    def __init__(self):
        # 获取账户信息
        yam = HandleYaml(os.path.join(CONF_PATH, "security.yaml"))
        security_data = yam.read()

        super().__init__(
            host=security_data["MYSQL"]["HOST"],
            port=security_data["MYSQL"]["PORT"],
            user=security_data["MYSQL"]["USER"],
            password=security_data["MYSQL"]["PWD"],
            database=security_data["MYSQL"]["NAME"],
            charset="utf8",
            cursorclass=pymysql.cursors.DictCursor
        )


class MidHandler:
    """
    中间层。common和调用的中间层。
    使用项目的配置数据， 填充common模块。
    作用：
        1. 隔离代码，让common更通用
        2. 使用common代码更加简单，少调用
    """
    # 获取配置文件中的数据
    yam = HandleYaml(os.path.join(CONF_PATH, "conf.yaml"))
    conf_data = yam.read()

    # 获取账户信息
    # 获取账户信息
    yam = HandleYaml(os.path.join(CONF_PATH, "security.yaml"))
    security_data = yam.read()

    # 初始化log
    log = get_logger(file=os.path.join(LOG_PATH, conf_data["LOG"]["FILENAME"]),
                     name=conf_data["LOG"]["NAME"],
                     level=conf_data["LOG"]["LEVEL"],
                     handler_level=conf_data["LOG"]["HANDLER_LEVEL"],
                     file_level=conf_data["LOG"]["FILE_LEVEL"],
                     fmt=conf_data["LOG"]["FMT"])

    # excel对象
    # 获取excel的路径
    excel_file = os.path.join(DATA_PATH, "case.xlsx")
    excel = HandleExcel(excel_file)

    # 数据库  下面这种写法是重命名
    db_class = MidDBHandler

    # --- 需要动态替换的数据 ---


    # --- ---- ---

    @classmethod
    def replace_data(cls, string, pattern=r"#(.*?)#"):
        """
        动态替换数据的方法
        :param string: 需要替换的字符串
        :param pattern: 正则表达式匹配规则
        :return: 替换后的字符串
        """
        res = re.finditer(pattern=pattern, string=string)
        for i in res:
            string = string.replace(i.group(), str(getattr(cls, i.group(1))))
        return string


if __name__ == "__main__":
    pass