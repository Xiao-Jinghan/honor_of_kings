import pymysql

def create_attribute_bonus_table(host, user, password, database):
    # 创建数据库连接
    connection = pymysql.connect(host=host,
                                   user=user,
                                   password=password,
                                   database=database,
                                  )

    try:
        with connection.cursor() as cursor:
            # 创建表的 SQL 语句
            create_table_sql = """
            CREATE TABLE IF NOT EXISTS attribute_bonus_information (
                passive_id INT AUTO_INCREMENT NOT NULL,
                name VARCHAR(255) NOT NULL,
                passive_skill_name VARCHAR(255) NOT NULL,
                bonus_attribute ENUM('physical_attack', 'magic_attack', 'attack_speed', 'critical_strike', 'physical_lifesteal', 'cooldown_reduction', 
                                     'max_mana', 'mana_per_5_seconds', ' health_per_5_seconds', 'max_health', 'physical_defense', 'magic_defense', 'movement_speed', 
                                     'extra_ealth', 'extra_physical_attack', 'extra_magic_attack') DEFAULT NULL,
                base_bonus_value FLOAT DEFAULT 0,
                bonus_percent_value FLOAT DEFAULT 0,
                bonus_value_or_lower_bound FLOAT DEFAULT 0,
                bonus_upper_bound FLOAT DEFAULT 0,
                bonus_target_attribute ENUM('physical_attack', 'magic_attack', 'attack_speed', 'critical_strike', 'physical_lifesteal', 'cooldown_reduction', 
                                           'max_mana', 'mana_per_5_seconds', 'health_per_5_seconds', 'max_health', 'physical_defense', 'magic_defense', 'movement_speed', 
                                           'physical_penetration', 'magic_penetration', 'magic_lifesteal', 'tenacity', 'physical_damage_reduction', 
                                           'main_attribute', 'summoner_skill_cooldown', 'critical_strike_effect') DEFAULT NULL,
                hero_type ENUM('melee', 'ranged', 'all') DEFAULT 'all',
                PRIMARY KEY (passive_id),
                FOREIGN KEY (name, passive_skill_name) REFERENCES passive_skill_description(name, passive_skill_name)
                    ON DELETE CASCADE
                    ON UPDATE CASCADE
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
            """

            # 执行创建表的 SQL 语句
            cursor.execute(create_table_sql)
            connection.commit()
            print("Attribute bonus information table created successfully!")

    finally:
        connection.close()

# 调用函数创建增加属性信息表
#create_attribute_bonus_table(host='localhost', user='root', password='password', database='damage_calculation')
