import pymysql

def create_inscription_information_table(host, user, password, database):
    # 创建数据库连接
    connection = pymysql.connect(host=host,
                                   user=user,
                                   password=password,
                                   database=database,
                                   charset='utf8mb4')

    try:
        with connection.cursor() as cursor:
            # 创建铭文信息表的 SQL 语句
            create_table_sql = """
            CREATE TABLE IF NOT EXISTS inscription_information (
                inscription_name VARCHAR(30) NOT NULL,
                inscription_type ENUM('red', 'green', 'blue') NOT NULL,
                physical_attack FLOAT NOT NULL DEFAULT 0,
                physical_penetration FLOAT NOT NULL DEFAULT 0,
                physical_lifesteal FLOAT NOT NULL DEFAULT 0,
                physical_defense FLOAT NOT NULL DEFAULT 0,
                magical_attack FLOAT NOT NULL DEFAULT 0,
                magical_penetration FLOAT NOT NULL DEFAULT 0,
                magical_lifesteal FLOAT NOT NULL DEFAULT 0,
                magical_defense FLOAT NOT NULL DEFAULT 0,
                attack_speed FLOAT NOT NULL DEFAULT 0,
                crit_rate FLOAT NOT NULL DEFAULT 0,
                crit_damage FLOAT NOT NULL DEFAULT 0,
                max_health FLOAT NOT NULL DEFAULT 0,
                hp_regen_per_5s FLOAT NOT NULL DEFAULT 0,
                movement_speed FLOAT NOT NULL DEFAULT 0,
                cooldown_reduction FLOAT NOT NULL DEFAULT 0,
                PRIMARY KEY (inscription_name)
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
            """

            # 执行创建表的 SQL 语句
            cursor.execute(create_table_sql)
            connection.commit()
            print("Inscription information table created successfully!")

    finally:
        connection.close()

# 调用函数创建铭文信息表
create_inscription_information_table(host='localhost', user='root', password='jichenyu666.', database='damage_calculation')
