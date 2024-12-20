import pymysql
import os
import csv


def insert_attribute_bonus_information(host, user, password, database):
    # 连接到MySQL数据库
    try:
        connection = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            charset='utf8mb4'
        )

        cursor = connection.cursor()

        # 文件路径，假设equipment_information.csv文件存放在当前目录的data文件夹中
        file_path = os.path.join(os.path.dirname(os.getcwd()), 'data', 'attribute_bonus_information.csv')

        # 打开CSV文件并读取数据
        with open(file_path, mode='r', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # 跳过表头

            # 插入数据
            for row in csv_reader:
                # 每一行数据有10个字段
                row = row[:10]
                row = [None if x == '' else x for x in row]
                sql = """
                INSERT INTO attribute_bonus_information (name,passive_skill_name,bonus_attribute,base_bonus_value
                                                        ,bonus_percent_value,bonus_target_attribute,bonus_value_or_lower_bound,bonus_upper_bound
                                                        ,hero_type,passive_id)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
                cursor.execute(sql, row)

        # 提交事务
        connection.commit()
        print("Data inserted successfully!")

    except Exception as e:
        print(f"Error occurred: {e}")
        connection.rollback()

    finally:
        # 关闭数据库连接
        cursor.close()
        connection.close()


# 调用函数
#insert_insert_attribute_bonus_information(host='localhost', user='root', password='password', database='database')