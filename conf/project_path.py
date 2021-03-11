"""
======================================
Author: Flora.Chen
Time: 2021/3/8 13:47
~ _ ~ ~ _ ~ ~ _ ~ ~ _ ~ ~ _ ~ ~ _ ~ 
======================================
"""
import os
# 项目根目录
PROJECT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 通用模块目录
COMMON_PATH = os.path.join(PROJECT_PATH, "common")

# 配置模块目录
CONF_PATH = os.path.join(PROJECT_PATH, "conf")

# 数据模块目录
DATA_PATH = os.path.join(PROJECT_PATH, "data")

# 日志模块目录
LOG_PATH = os.path.join(PROJECT_PATH, "log")
if not os.path.exists(LOG_PATH):
    os.mkdir(LOG_PATH)

# 报告模块目录
REPORT_PATH = os.path.join(PROJECT_PATH, "report")
if not os.path.exists(REPORT_PATH):
    os.mkdir(REPORT_PATH)

# 测试用例模块
TESTCASE_PATH = os.path.join(PROJECT_PATH, "test")

# 中间件模块
MIDDLEWARE_PATH = os.path.join(PROJECT_PATH, "middleware")

if __name__ == "__main__":
    print(LOG_PATH)
    print(REPORT_PATH)