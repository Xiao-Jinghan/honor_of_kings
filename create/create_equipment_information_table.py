import pymysql

def create_equipment_information_table(host, user, password, database):
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
            CREATE TABLE IF NOT EXISTS equipment_information (
                name VARCHAR(255) NOT NULL,
                type ENUM('Attack', 'Magic', 'Defense', 'Movement', 'Jungle', 'Support') NOT NULL,
                price FLOAT NOT NULL DEFAULT 0,
                physical_attack FLOAT NOT NULL DEFAULT 0,
                magic_attack FLOAT NOT NULL DEFAULT 0,
                attack_speed FLOAT NOT NULL DEFAULT 0,
                critical_strike FLOAT NOT NULL DEFAULT 0,
                physical_lifesteal FLOAT NOT NULL DEFAULT 0,
                cooldown_reduction FLOAT NOT NULL DEFAULT 0,
                max_mana FLOAT NOT NULL DEFAULT 0,
                mana_per_5_seconds FLOAT NOT NULL DEFAULT 0,
                health_per_5_seconds FLOAT NOT NULL DEFAULT 0,
                max_health FLOAT NOT NULL DEFAULT 0,
                physical_defense FLOAT NOT NULL DEFAULT 0,
                magic_defense FLOAT NOT NULL DEFAULT 0,
                movement_speed FLOAT NOT NULL DEFAULT 0,
                PRIMARY KEY (name)
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
            """

            # 执行创建表的 SQL 语句
            cursor.execute(create_table_sql)
            connection.commit()
            print("Equipment information table created successfully")

    finally:
        connection.close()

#create_equipment_information_table(host='localhost', user='root', password='password', database='damage_calculation')