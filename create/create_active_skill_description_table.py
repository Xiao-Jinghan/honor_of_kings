import pymysql

def create_active_skill_description_table(host, user, password, database):
    # 创建数据库连接
    connection = pymysql.connect(host=host,
                                   user=user,
                                   password=password,
                                   database=database,
                                   charset='utf8mb4')

    try:
        with connection.cursor() as cursor:
            # 创建表的 SQL 语句
            create_table_sql = """
            CREATE TABLE IF NOT EXISTS active_skill_description (
                name VARCHAR(255) NOT NULL,
                active_skill_name VARCHAR(255) NOT NULL,
                active_skill_description VARCHAR(255) NOT NULL,
                active_skill_cd FLOAT NOT NULL DEFAULT 0,
                PRIMARY KEY (name, active_skill_name),
                FOREIGN KEY (name) REFERENCES equipment_information(name)
                    ON DELETE CASCADE
                    ON UPDATE CASCADE
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
            """

            # 执行创建表的 SQL 语句
            cursor.execute(create_table_sql)
            connection.commit()
            print("Active skill description table created successfully!")

    finally:
        connection.close()

# 调用函数创建主动技能表
#create_active_skill_description_table(host='localhost', user='root', password='password', database='damage_calculation')
