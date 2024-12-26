import pymysql


# 定义连接数据库的函数
def create_direct_damage_information_table(host, user, password, database):
    try:
        # 连接到数据库
        connection = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )

        with connection.cursor() as cursor:
            # 定义 SQL 语句创建表
            create_table_query = """
            CREATE TABLE IF NOT EXISTS direct_damage_information (
                passive_id INT PRIMARY KEY AUTO_INCREMENT,  -- 被动技能 ID，主键
                name VARCHAR(255) NOT NULL,  -- 装备名称
                passive_skill_name VARCHAR(255) NOT NULL,  -- 被动技能名称
                bonus_attribute ENUM('physical_attack', 'magic_attack', 'attack_speed', 'critical_strike', 
                                     'physical_lifesteal', 'cooldown_reduction', 'max_mana', 'mana_per_5_seconds', 
                                     'health_per_5_seconds', 'max_health', 'physical_defense', 'magic_defense', 
                                     'movement_speed', 'extra_health', 'extra_physical_attack', 'extra_magic_attack') NOT NULL,  -- 加成属性
                base_bonus_value FLOAT DEFAULT 0,  -- 加成基础值
                bonus_percent_value FLOAT DEFAULT 0,  -- 加成属性百分值
                bonus_target_attribute ENUM('cause_physical_damage', 'cause_magic_damage', 'cause_real_damage') NOT NULL,  -- 被加成属性
                passive_skill_cd FLOAT DEFAULT 0,  -- 被动技能冷却时间
                hero_type ENUM('melee', 'ranged', 'all') DEFAULT 'all',  -- 英雄类型
                FOREIGN KEY (equipment_name, passive_skill_name) REFERENCES passive_skill_description(name, passive_skill_name)  -- 外键约束
            );
            """
            # 执行 SQL 语句
            cursor.execute(create_table_query)

            # 提交事务
            connection.commit()

            print("Direct damage information table created successfully")

    except pymysql.MySQLError as e:
        print(f"ERROR: {e}")
    finally:
        # 关闭数据库连接
        connection.close()


# 调用函数，输入数据库连接参数
#create_direct_damage_information_table(user='your_user', host='your_host', password='your_password', database='your_database')
