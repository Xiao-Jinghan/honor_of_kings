import pymysql

def create_overlay_information_table(host, user, password, database):
    # 连接到数据库
    connection = pymysql.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )

    try:
        with connection.cursor() as cursor:
            # 创建表的SQL语句
            create_table_query = """
            CREATE TABLE IF NOT EXISTS overlay_information_table (
                passive_id INT AUTO_INCREMENT NOT NULL,
                name VARCHAR(255) NOT NULL,
                passive_skill_name VARCHAR(255) NOT NULL,
                overlay_condition ENUM('attack','kill_wild','damage_hero','magic_attack','critical_strike','injured',
                                        'lose_health', 'physical_attack')
                    DEFAULT NULL,
                trigger_times FLOAT NOT NULL,
                result ENUM('cause_magic_damage', 'slow', 'magic_attack', 'max_health', 'physical_attack', 
                            'cooldown_reduction', 'magic_penetration', 'damage_increase_ratio', 'physical_penetration', 
                            'attack_speed', 'critical_strike_effect', 'increase_damage', 'movement_speed', 'health_regeneration_effect')
                            NOT NULL,
                max_layer   INT DEFAULT -1,
                max_result ENUM('attack_bonus_damage','attack_bonus_magic_damage','attack_bonus_physical_damage')
                            DEFAULT NULL,
                max_bonus_attribute ENUM('physical_attack', 'magic_attack', 'attack_speed', 'critical_strike', 
                                        'physical_lifesteal', 'cooldown_reduction', 'max_mana', 'mana_per_5_seconds',
                                         'health_per_5_seconds', 'max_health', 'physical_defense', 'magic_defense',
                                         'movement_speed', 'extra_health', 'extra_physical_attack', 'extra_magic_attack') 
                                    DEFAULT NULL,              
                max_base_bonus_value FLOAT DEFAULT 0,
                max_bonus_percent_value FLOAT DEFAULT 0,
                bonus_value_or_lower_bound FLOAT DEFAULT 0,
                bonus_upper_bound FLOAT DEFAULT 0,
                duration FLOAT DEFAULT 0,
                passive_skill_cd FLOAT DEFAULT 0,
                PRIMARY KEY (passive_id),
                FOREIGN KEY (name, passive_skill_name) 
                    REFERENCES passive_skill_description(name, passive_skill_name)
                    ON DELETE CASCADE
                    ON UPDATE CASCADE
            );
            """
            # 执行创建表的SQL语句
            cursor.execute(create_table_query)
            print("Overlay information table created successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # 关闭数据库连接
        connection.close()

# 示例：调用函数创建表，传入相应数据库参数
# create_overlay_information_table('localhost', 'your_username', 'your_password', 'your_database')
