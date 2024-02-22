import pymysql

from config import *



class MySql:

    def __init__(self):
        # 连接到数据库
        # self.conn = pymysql.connect(host=HOST,port=PORT, user=USER, password=PASSWORD, db=DB, charset=CHARSET)
        # db要操作的数据库
        self.conn = pymysql.connect(host=host, port=port, user=user, password=password, charset=charset,db =db)
        self.cursor = self.conn.cursor() # 游标对象用于执行SQL语句和获取结果。

    def close_db(self):
        # 关闭数据库连接
        self.conn.close()
        print("关闭数据库")

    # 插入数据
    def insert_data(self, table, data):
        """
        增加数据
        :param table: 要操作的表名："landlord",
        :param data: 数据字典格式，示例:{"landlord_phone":"6666", "house_number":"101","Landlord_name": "Jerry","password":"男"}
        :return:
        """
        placeholders = ', '.join(['%s'] * len(data))  # 根据数据的长度替换成格式符
        columns = ', '.join(data.keys())  # 拆分字典的key值
        sql = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
        try:
            self.cursor.execute(sql, tuple(data.values()))
            #  self.cursor.execute（INSERT INTO landlord (landlord_phone, house_number, Landlord_name, password)
            #  VALUES (%s, %s, %s, %s)，('6666', '101', 'Jerry', '男') ）
            self.conn.commit()
            print("数据插入成功！")
        except Exception as e:
            self.conn.rollback()
            print(f"数据插入失败：{e}")
        finally:
            self.cursor.close()#关闭游标对象

    # 删除数据
    def delete_data(self, table, condition):
        """
        删除数据
        :param table: 需要操作的表
        :param condition: 条件，示例："house_number='22'" 多条件：and
        :return:
        """
        sql = f"DELETE FROM {table} WHERE {condition}"
        try:
            self.cursor.execute(sql)
            self.conn.commit()
            if self.cursor.rowcount:
                print("操作成功！有{}行相关数据被删除！".format(self.cursor.rowcount))
            else:
                print("失败，可操作的数据显示{}行".format(self.cursor.rowcount))
        except Exception as e:
            self.conn.rollback()
            print(f"数据删除失败：{e}")
        finally:
            self.cursor.close()
            print("关闭游标")

    # 更新数据
    def update_data(self, table, condition, data):
        """
        更新数据( "landlord","house_number='101'", {"password":"123"} )

        :param table: 需要更新的表名
        :param condition: 更新的条件，符合这个条数据的列，示例："house_number='101'"
        :param data: 要修改的数据列字典格式，示例：{"password":"123"}
        :return:
        """
        placeholders = ', '.join([f"{key}=%s" for key in data.keys()])
        sql = f"UPDATE {table} SET {placeholders} WHERE {condition}"
        try:
            self.cursor.execute(sql, tuple(data.values()))
            print(sql, tuple(data.values()))
            self.conn.commit()
            if self.cursor.rowcount:
                print("成功！有{}行相关数据被更新！".format(self.cursor.rowcount))
            else:
                print("失败，可操作的数据显示{}行".format(self.cursor.rowcount))
        except Exception as e:
            self.conn.rollback()
            print(f"数据更新失败：{e}")
        finally:
            self.cursor.close()

    # 查询数据
    def select_data(self, table, condition=""):
        """
        查询数据
        :param table: 要操作的数据库的表
        :param condition: 查询条件，默认为空。查询所有数据。示例：" password='男' "
        :return:
        """
        sql = f"SELECT * FROM {table}"
        if condition:
            sql += f" WHERE {condition}"
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            if len(result) > 0:
                print("查询结果如下：")
                for row in result:
                    print(row)
            else:
                print("暂无查询结果！")

        except Exception as e:
            print(f"数据查询出错：{e}")
        finally:
            self.cursor.close()



"""
你好，我叫**，上一家公司是浙江巨点智慧光线有限公司，担任测试工程师，主要负责项目的测试，文档输出，项目维护工作。
巨点科技主要业务是：智慧园区，三维可视化，展厅中控，管理后台，小程序
离职原因：公司业务转型，工作内容偏开发和维护，无法获得更大的发展空间
未来方向：在工作中学习更多积累更多的知识点，在业余学习的内容应用到工作中，在测试行业中继续发展下去
"""
# MySql().insert_data("landlord",
# {"landlord_phone":"6666", "house_number":"101","Landlord_name": "Jerry","password":"男"})
# MySql().select_data("landlord","password='男'")
# MySql().update_data( "landlord","house_number='101'", {"password":"123"} )
# MySql().delete_data( "landlord","house_number='101' and password='123'")
# MySql().close_db()
