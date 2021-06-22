# coding: utf-8
# author: hmk
import pymysql
from common.ReadConfig import ReadConfig

class HandleMysql:
    def __init__(self):
        self.data = ReadConfig()

    def conn_mysql(self):
        """连接数据库"""
        host = self.data.get_db("host")
        username = self.data.get_db("username")
        password = self.data.get_db("password")
        db_name = self.data.get_db("db_name")
        charset =self.data.get_db("charset")
        self.conn = pymysql.connect(host=host, user=username, password=password, db=db_name,charset=charset)
        self.cur = self.conn.cursor()

    def execute_sql(self, sql, data):
        """执行操作数据的相关sql"""
        self.conn_mysql()
        self.cur.execute(sql, data)
        self.conn.commit()

    def search(self, sql):
        """执行查询sql"""
        self.conn_mysql()
        self.cur.execute(sql)
        return self.cur.fetchall()

    def close_mysql(self):
        """关闭数据库连接"""
        self.cur.close()
        self.conn.close()


if __name__ == '__main__':
    test = HandleMysql()
    sql = "insert into user values('ccc','222')"
    for i in test.execute_sql(sql):
        print(i)