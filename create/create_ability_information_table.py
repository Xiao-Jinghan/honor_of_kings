import pymysql

def create_ability_information_table(host, user, password, database):
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
            CREATE TABLE IF NOT EXISTS ability_information (
                passive_id INT AUTO_INCREMENT NOT NULL,
                name VARCHAR(255) NOT NULL,
                passive_skill_name VARCHAR(255) NOT NULL,
                trigger_condition ENUM('hit','hit_hero','use','hit_movement_lower_hero')
                    DEFAULT NULL,
                effect ENUM('enemy_hero', 'enemy', 'aoe', 'self', 'enemy_melee_hero', 'enemy_ranged_hero') 
                    DEFAULT NULL,
                bonus_attribute ENUM('target_max_health', 'target_current_health', 'physical_attack', 'magic_attack') 
                    DEFAULT NULL,
                base_bonus_value FLOAT DEFAULT 0,
                bonus_percent_value FLOAT DEFAULT 0,
                bonus_value_or_lower_bound FLOAT DEFAULT 0,
                bonus_upper_bound FLOAT DEFAULT 0,
                bonus_target_attribute ENUM('slow', 'reduce_self_damage', 'bonus_magic_damage', 'movement_speed', 
                                'next_basic_attack_bonus_physical_damage', 'next_basic_attack_bonus_magic_damage',
                                'next_basic_attack_slow', 'attack_speed_for_next_3_basic_attacks', 'cause_magic_damage') 
                                             DEFAULT NULL,
                duration FLOAT DEFAULT 0,
                time_limit FLOAT DEFAULT 0,
                frequency_limit FLOAT DEFAULT 0,
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
            print("Ability information table created successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # 关闭数据库连接
        connection.close()

# 示例：调用函数创建表，传入相应数据库参数
# create_ability_information_table('localhost', 'your_username', 'your_password', 'your_database')
