import pymysql

def create_hurt_information_table(host, user, password, database):
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
            CREATE TABLE IF NOT EXISTS hurt_information_table (
                passive_id INT AUTO_INCREMENT NOT NULL,
                name VARCHAR(255) NOT NULL,
                passive_skill_name VARCHAR(255) NOT NULL,
                time_limit FLOAT DEFAULT 0,  
                hurt_condition ENUM('single_hurt','physical_hurt','magic_hurt','hurt','self_health')
                    NOT NULL,
                condition_name ENUM('current_health','max_health','physical_damage','magic_damage')
                    DEFAULT NULL,
                condition_type ENUM('lower','higher') DEFAULT NULL,
                condition_value FLOAT DEFAULT 0,               
                bonus_attribute ENUM('max_health','physical_hurt_value') DEFAULT 0,
                base_bonus_value FLOAT DEFAULT 0,
                bonus_percent_value FLOAT DEFAULT 0,
                bonus_value_or_lower_bound FLOAT DEFAULT 0,
                bonus_upper_bound FLOAT DEFAULT 0,
                bonus_target_attribute ENUM('cause_magic_damage','cause_physical_damage','aoe_slow','aoe_reduce_attack_speed',
                                            'reduce_attacker_attack_speed','health_every_second','increase_damage') 
                                             DEFAULT NULL,
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
            print("Hurt information table created successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # 关闭数据库连接
        connection.close()

# 示例：调用函数创建表，传入相应数据库参数
# create_hurt_information_table('localhost', 'your_username', 'your_password', 'your_database')
