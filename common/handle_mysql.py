"""
======================================
Author: Flora.Chen
Time: 2021/3/11 21:51
~ _ ~ ~ _ ~ ~ _ ~ ~ _ ~ ~ _ ~ ~ _ ~ 
======================================
"""
import pymysql


class DBHandler:
    """
    数据库操作
    """

    def __init__(self,
                 host=None,
                 port=None,
                 user=None,
                 password=None,
                 database=None,
                 charset="utf8",
                 cursorclass=pymysql.cursors.DictCursor  # 加上这个返回的就是字典
                 ):
        """
        初始化方法中， 连接到数据库
        """

        # 建立连接
        self.conn = pymysql.connect(host=host,
                                    port=port,
                                    user=user,
                                    password=password,
                                    database=database,
                                    charset=charset,
                                    cursorclass=cursorclass
                                    )

    def query_all(self, sql):
        """
        查询所有符合sql条件的数据
        :param sql: 执行的sql
        :return: 查询结果
        """
        # 创建一个游标对象
        self.cursor = self.conn.cursor()
        self.conn.commit()
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        self.cursor.close()
        return data

    def query_one(self, sql):
        """
        查询符合sql条件的数据的第一条数据
        :param sql: 执行的sql
        :return: 返回查询结果的第一条数据
        """
        # 创建一个游标对象
        self.cursor = self.conn.cursor()

        self.conn.commit()
        self.cursor.execute(sql)
        data = self.cursor.fetchone()
        self.cursor.close()
        return data

    def insert(self, sql):
        """
        插入数据
        :param sql: 执行的sql
        """
        # 创建一个游标对象
        self.cursor = self.conn.cursor()

        self.cursor.execute(sql)
        # 提交  只要数据库更新就要commit
        self.conn.commit()

        self.cursor.close()

    def update(self, sql):
        """
        更新数据
        :param sql: 执行的sql
        """
        # 创建一个游标对象
        self.cursor = self.conn.cursor()

        self.cursor.execute(sql)
        # 提交 只要数据库更新就要commit
        self.conn.commit()

        self.cursor.close()

    def query(self, sql, one=True):
        """
        根据传值决定查询一条数据还是所有
        :param one: 默认True. True查一条数据，否则查所有
        :return:
        """
        if one:
            return self.query_one(sql)
        else:
            return self.query_all(sql)

    def close(self):
        """
        断开游标，关闭数据库
        :return:
        """
        self.conn.close()
