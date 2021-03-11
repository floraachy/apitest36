"""
======================================
Author: Flora.Chen
Time: 2021/3/8 15:37
~ _ ~ ~ _ ~ ~ _ ~ ~ _ ~ ~ _ ~ ~ _ ~ 
======================================
"""
import yaml, os


class HandleYaml:
    """
    读取yaml数据，以及往yaml文件中写入数据
    """
    def __init__(self, file):
        """
        初始化yaml文件，如果不存在则创建
        :param file: 文件绝对路径
        """
        if not os.path.exists(file):
            with open(file, mode="a", encoding="utf-8"):
                print("{}文件创建成功~".format(file))
        self.file = file

    def read(self):
        """
        读取yaml文件数据
        :return: 读取到的数据
        """
        with open(file=self.file, mode="r", encoding="UTF-8") as f:
            return yaml.load(f, Loader=yaml.SafeLoader)

    def write(self, data, mode="a"):
        """
        往yaml文件中写入数据，默认是追加写入
        :param data: 要写入的数据
        :param mode: 写入模式
        :return:
        """
        with open(self.file, mode=mode, encoding="utf-8") as f:
            yaml.dump(data, f)

if __name__ == "__main__":
    yam = HandleYaml("test.yaml")
    yam.read()
    yam.write("test: test")
