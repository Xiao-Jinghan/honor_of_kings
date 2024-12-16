import pymysql
import os
import csv


def insert_equipment_information(host, user, password, database):
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
        file_path = os.path.join(os.path.dirname(os.getcwd()), 'data', 'equipment_information.csv')

        # 打开CSV文件并读取数据
        with open(file_path, mode='r', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # 跳过表头

            # 插入数据
            for row in csv_reader:
                # 每一行数据有16个字段
                sql = """
                INSERT INTO equipment_information (name,type,price,physical_attack,magic_attack,attack_speed
                                                    ,critical_strike,physical_lifesteal,cooldown_reduction,max_mana
                                                    ,mana_per_5_seconds,health_per_5_seconds,max_health,physical_defense
                                                    ,magic_defense,movement_speed)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
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
#insert_equipment_information(host='localhost', user='root', password='password', database='database')