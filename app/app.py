import pymysql
import tkinter as tk
from tkinter import ttk
from hero.hero import HeroInputForm

# 连接到 MySQL 数据库并获取指定类型的数据
def get_data_by_type(equipment_type):
    # 连接到 MySQL 数据库
    conn = pymysql.connect(
        host="localhost",  # 数据库主机地址
        user="root",  # 数据库用户名
        password="jichenyu666.",  # 数据库密码
        database="damage_calculation"  # 使用的数据库
    )
    cursor = conn.cursor()

    # 根据类型查询数据
    query = '''
        SELECT name, price, physical_attack, magic_attack, attack_speed, critical_strike, 
               physical_lifesteal, cooldown_reduction, max_mana, mana_per_5_seconds, 
               health_per_5_seconds, max_health, physical_defense, magic_defense, movement_speed
        FROM equipment_information WHERE type = %s
    '''
    cursor.execute(query, (equipment_type,))

    # 获取查询结果
    rows = cursor.fetchall()

    # 关闭连接
    conn.close()

    return rows


def get_data_by_name(names):
    # 连接到 MySQL 数据库
    conn = pymysql.connect(
        host="localhost",  # 数据库主机地址
        user="root",  # 数据库用户名
        password="jichenyu666.",  # 数据库密码
        database="damage_calculation"  # 使用的数据库
    )
    cursor = conn.cursor()

    # 创建一个空列表用于存储结果
    results = []

    # 遍历 names 数组，对每个名称执行查询
    for name in names:
        query = '''
            SELECT name, price, physical_attack, magic_attack, attack_speed, critical_strike, 
                   physical_lifesteal, cooldown_reduction, max_mana, mana_per_5_seconds, 
                   health_per_5_seconds, max_health, physical_defense, magic_defense, movement_speed
            FROM equipment_information WHERE name = %s
        '''
        cursor.execute(query, (name,))

        # 获取查询结果
        row = cursor.fetchone()  # 使用 fetchone() 获取单个结果

        if row:
            results.append(row)  # 如果有结果，则将其添加到列表中
        else:
            results.append(None)  # 如果没有结果，可以存储 None 或者其他指示没有数据的值

    # 关闭连接
    conn.close()

    return results

# 从 passive_skill_description 表获取被动技能名称和描述
def get_passive_skills_by_name(name):
    # 连接到 MySQL 数据库
    conn = pymysql.connect(
        host="localhost",  # 数据库主机地址
        user="root",  # 数据库用户名
        password="jichenyu666.",  # 数据库密码
        database="damage_calculation"  # 使用的数据库
    )
    cursor = conn.cursor()

    # 查询被动技能
    query = '''
        SELECT passive_skill_name, passive_skill_description 
        FROM passive_skill_description WHERE name = %s
    '''
    cursor.execute(query, (name,))

    # 获取查询结果
    skills = cursor.fetchall()

    # 关闭连接
    conn.close()

    return skills

def get_active_skills_by_name(name):
    # 连接到 MySQL 数据库
    conn = pymysql.connect(
        host="localhost",  # 数据库主机地址
        user="root",  # 数据库用户名
        password="jichenyu666.",  # 数据库密码
        database="damage_calculation"  # 使用的数据库
    )
    cursor = conn.cursor()

    # 查询被动技能
    query = '''
        SELECT active_skill_name, active_skill_description 
        FROM active_skill_description WHERE name = %s
    '''
    cursor.execute(query, (name,))

    # 获取查询结果
    skills = cursor.fetchall()

    # 关闭连接
    conn.close()

    return skills
# 主界面
class App:
    def __init__(self, root):

        self.root = root
        self.root.title("Game Equipment Categories")

        # 设置窗口大小
        self.root.geometry("1200x800")

        # 创建按钮栏
        self.button_frame = ttk.Frame(self.root)
        self.button_frame.pack(side="top", fill="x", padx=10, pady=10)

        # 按钮列表
        self.buttons = [
            ("攻击", "Attack"),
            ("法术", "Magic"),
            ("防御", "Defense"),
            ("移动", "Movement"),
            ("打野", "Jungle"),
            ("辅助", "Support")
        ]

        # 按钮对应的框架存储
        self.frames = {}

        # 为每个按钮创建对应的按钮和切换界面功能
        for text, category in self.buttons:
            button = ttk.Button(self.button_frame, text=text, command=lambda c=category: self.show_category(c))
            button.pack(side="left", padx=5, pady=5, expand=True)

        # 初始显示第一个界面
        self.current_frame = None
        self.selected = []
        self.enemy_selected = []
        self.hero = None
        self.enemy_hero = None
    def update_callback(self,category_name,name,flag,window = None):
        # 如果当前有显示的框架，先移除它
        if flag == 1:
            if len(self.hero.equipment) < 6:
                self.hero.equipment.append(name)
        elif flag == 2:
            if len(self.enemy_hero.equipment) < 6:
                self.enemy_hero.equipment.append(name)
        elif flag == 3:
            if len(self.hero.equipment) > 0:
                self.hero.equipment.remove(name)
                window.destroy()
        elif flag == 4:
            if len(self.enemy_hero.equipment) > 0:
                self.enemy_hero.equipment.remove(name)
                window.destroy()
        if self.current_frame:
            self.current_frame.pack_forget()
        # 创建对应类别的界面并显示
        self.frames[category_name] = self.create_category_frame(self.root, category_name,self.show_equipment_attributes)
        self.frames[category_name].pack(fill="both", expand=True, padx=10, pady=10)
        self.current_frame = self.frames[category_name]
    def create_hero(self, flag):
        if flag==1:
            if self.hero ==None:
                self.hero = HeroInputForm()
            self.hero.create_form()
        elif flag ==2:
            if self.enemy_hero == None:
                self.enemy_hero = HeroInputForm()
            self.enemy_hero.create_form()
    def calculate_attack_damage(self):
        self.hero.update()
        self.enemy_hero.update()
        attack = self.hero.attributes['physical_attack'][0]+self.hero.attributes['physical_attack'][1]
        defense = self.enemy_hero.attributes['physical_defense'][0]+self.enemy_hero.attributes['physical_defense'][1]
        per1 = self.hero.attributes['physical_penetration'][0]+self.hero.attributes['physical_penetration'][1]
        per2 = self.hero.attributes['physical_penetration'][2] /100
        print(attack,defense,per1,per2)
        if per1>defense:
            damage = attack
        else:
            result = 1 - ((defense-per1)*(1-per2))/((defense-per1)*(1-per2)+600)
            damage = attack * result
        window = tk.Tk()
        window.title("普通攻击伤害值")

        # 创建标签，显示"普攻伤害值为: "和计算出的伤害值
        label = tk.Label(window, text=f"普攻伤害值为: {damage:.2f}", font=("Arial", 14))
        label.pack(padx=20, pady=20)

        # 按钮，点击后关闭窗口
        button = tk.Button(window, text="关闭", command=window.destroy)
        button.pack(padx=10, pady=10)

    def create_category_frame(self,window, category_name, callback):
        # 创建一个框架
        frame = ttk.Frame(window)

        # 获取当前类型的数据
        data = get_data_by_type(category_name)
        select = None
        enemy_select = None
        if self.hero !=None:
            if self.hero.equipment != []:
                select = get_data_by_name(self.hero.equipment)
        if self.enemy_hero!=None:
            if self.enemy_hero.equipment !=[]:
                enemy_select = get_data_by_name(self.enemy_hero.equipment)
        #print('create',self.selected)
        #print('select',select)
        # 按价格将装备分为四列
        col1 = []  # 价格 <= 500
        col2 = []  # 500 < 价格 <= 900
        col3 = []  # 900 < 价格 <= 2050
        col4 = []  # 价格 > 2050
        col5 = []  # 若干个按钮,包括输入己方英雄数值, 敌方英雄数值以及开始计算的按键
        col6 = []  # 己方装备列
        col7 = []  # 敌方装备列
        for row in data:
            name, price, *_ = row
            if price <= 500:
                col1.append(row)
            elif price <= 900:
                col2.append(row)
            elif price <= 2050:
                col3.append(row)
            else:
                col4.append(row)
        col5.append('输入本方英雄数值')
        col5.append('输入敌方英雄数值')
        col5.append('计算普攻伤害')
        if select != None:
            for row in select:
                name, price, *_ = row
                col6.append(row)
        if enemy_select != None:
            for row in enemy_select:
                name, price, *_ = row
                col7.append(row)
        # 创建Canvas和Scrollbar来实现滚动功能
        canvas = tk.Canvas(frame)
        scrollbar = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=scrollbar.set)

        # 创建一个内部框架用于放置内容
        content_frame = ttk.Frame(canvas)

        # 将内部框架放入Canvas中
        canvas.create_window((0, 0), window=content_frame, anchor="nw")

        # 布局按钮：分别放入7列
        for equipment_list, col in zip([col1, col2, col3, col4, col5, col6, col7], range(7)):
            col_frame = ttk.Frame(content_frame)
            col_frame.grid(row=0, column=col, padx=10, pady=10, sticky="nsew")
            # 对于 col5，创建特定的按钮并绑定不同的回调函数
            if col == 4:  # 这里是针对 col5 的特殊情况
                button1 = tk.Button(col_frame, text=equipment_list[0], command=lambda: self.create_hero(1), relief="flat", bg="skyblue",
                                    fg="white", font=("Arial", 12))
                button1.grid(row=0, column=0, padx=10, pady=(60,5), sticky="ew")

                button2 = tk.Button(col_frame, text=equipment_list[1], command=lambda: self.create_hero(2), relief="flat", bg="skyblue",
                                    fg="white", font=("Arial", 12))
                button2.grid(row=1, column=0, padx=10, pady=5, sticky="ew")

                button3 = tk.Button(col_frame, text=equipment_list[2], command=lambda: self.calculate_attack_damage(), relief="flat", bg="skyblue",
                                    fg="white", font=("Arial", 12))
                button3.grid(row=2, column=0, padx=10, pady=5, sticky="ew")
            # 显示装备按钮
            elif col == 5:
                label = tk.Label(col_frame, text="己方装备", font=("Arial", 14, "bold"), fg="grey")
                label.grid(row=0, column=0, padx=10, pady=5, sticky="ew")
                for idx, (name, *_attributes) in enumerate(equipment_list):
                    pady = (60, 5) if idx == 0 else (5, 5)  # 如果是第一个按钮，设置 pady=30，否则为 pady=5
                    button = tk.Button(col_frame, text=name, width=10,
                                        command=lambda name=name: callback(name, category_name, 5))
                    button.grid(row=idx+1, column=0, padx=10, pady=pady, sticky="w")
            elif col == 6:
                label = tk.Label(col_frame, text="敌方装备", font=("Arial", 14, "bold"), fg="grey")
                label.grid(row=0, column=0, padx=10, pady=5, sticky="ew")
                for idx, (name, *_attributes) in enumerate(equipment_list):
                    pady = (60, 5) if idx == 0 else (5, 5)  # 如果是第一个按钮，设置 pady=30，否则为 pady=5
                    button = tk.Button(col_frame, text=name, width=10,
                                        command=lambda name=name: callback(name, category_name, 6))
                    button.grid(row=idx+1, column=0, padx=10, pady=pady, sticky="w")
            else:
                for idx, (name, *_attributes) in enumerate(equipment_list):
                    pady = (60, 5) if idx == 0 else (5, 5)  # 如果是第一个按钮，设置 pady=30，否则为 pady=5
                    button = tk.Button(col_frame, text=name, width=10,
                                        command=lambda name=name: callback(name, category_name,1))
                    button.grid(row=idx+1, column=0, padx=10, pady=pady, sticky="w")


        # 更新canvas的区域大小以适应内容
        content_frame.update_idletasks()  # 更新内容帧大小
        canvas.config(scrollregion=canvas.bbox("all"))  # 设置滚动区域大小

        # 布局滚动条和Canvas
        canvas.grid(row=0, column=0, sticky="nsew")
        scrollbar.grid(row=0, column=1, sticky="ns")

        # 确保frame的grid布局能够自适应窗口大小
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)

        # **修改部分：分割线的固定位置**
        # 让分割线在canvas滚动区域的外部固定，防止它被滚动
        separator = ttk.Separator(frame, orient="vertical")
        separator.grid(row=0, column=4, sticky="ns", padx=5)

        # 使每列平分窗口的宽度
        content_frame.grid_columnconfigure(0, weight=1)
        content_frame.grid_columnconfigure(1, weight=1)
        content_frame.grid_columnconfigure(2, weight=1)
        content_frame.grid_columnconfigure(3, weight=1)
        content_frame.grid_columnconfigure(4, weight=1)
        content_frame.grid_columnconfigure(5, weight=1)
        content_frame.grid_columnconfigure(6, weight=1)

        # 确保整个frame的布局能够自适应大小
        frame.grid_rowconfigure(0, weight=1)  # 设置frame的行宽度为自适应
        frame.grid_columnconfigure(0, weight=1)  # 设置frame的列宽度为自适应

        return frame
    # 点击装备名称按钮后，显示属性
    def show_equipment_attributes(self,name, category,num):
        # 获取装备详细信息
        conn = pymysql.connect(
            host="localhost",  # 数据库主机地址
            user="root",  # 数据库用户名
            password="jichenyu666.",  # 数据库密码
            database="damage_calculation"  # 使用的数据库
        )
        cursor = conn.cursor()

        # 查询装备详细信息
        query = '''
            SELECT name, price, physical_attack, magic_attack, attack_speed, critical_strike, 
                   physical_lifesteal, cooldown_reduction, max_mana, mana_per_5_seconds, 
                   health_per_5_seconds, max_health, physical_defense, magic_defense, movement_speed
            FROM equipment_information WHERE name = %s
        '''
        cursor.execute(query, (name,))

        equipment = cursor.fetchone()
        conn.close()

        # 创建一个新的窗口来显示该装备的详细信息
        attribute_window = tk.Toplevel()
        attribute_window.title(f"{equipment[0]} - Details")

        # 过滤掉值为 0 的属性并创建标签
        labels = [
            ("装备名称", equipment[0]), ("价格", equipment[1]), ("物理攻击", equipment[2]),
            ("法术攻击", equipment[3]), ("攻击速度", equipment[4]), ("暴击率", equipment[5]),
            ("物理吸血", equipment[6]), ("冷却缩减", equipment[7]),
            ("最大法力", equipment[8]), ("每5s回蓝", equipment[9]),
            ("每5s回血", equipment[10]), ("最大生命", equipment[11]),
            ("物理防御", equipment[12]), ("法术防御", equipment[13]),
            ("移速", equipment[14])
        ]

        row = 0
        for attr_name, attr_value in labels:
            if attr_value != 0:  # 只显示非零值的属性
                label = ttk.Label(attribute_window, text=f"{attr_name}: {attr_value}")
                label.grid(row=row, column=0, padx=10, pady=5, sticky="w")
                row += 1

        # 获取被动技能信息
        passive_skills = get_passive_skills_by_name(name)

        if passive_skills:
            ttk.Label(attribute_window).grid(row=row, column=0, padx=10, pady=5, sticky="w")
            row += 1
            for skill_name, skill_desc in passive_skills:
                ttk.Label(attribute_window, text=f"被动  {skill_name}: {skill_desc}").grid(row=row, column=0, padx=10,
                                                                                         pady=5, sticky="w")
                row += 1

        #获取主动技能信息
        active_skills = get_active_skills_by_name(name)
        if active_skills:
            ttk.Label(attribute_window).grid(row=row, column=0, padx=10, pady=5, sticky="w")
            row += 1
            for skill_name, skill_desc in active_skills:
                ttk.Label(attribute_window, text=f"主动  {skill_name}: {skill_desc}").grid(row=row, column=0, padx=10,
                                                                                         pady=5, sticky="w")
                row += 1

        add_button = tk.Button(attribute_window, text="添加到己方已选装备",
                                command=lambda: self.update_callback(category, name, 1))
        add_button.grid(row=row, column=0, padx=10, pady=5, sticky="w")
        if num == 5:
            add_button2 = tk.Button(attribute_window, text="删除该装备",
                                    command=lambda: self.update_callback(category, name, 3, attribute_window))
            add_button2.grid(row=row, column=1, padx=10, pady=5, sticky="w")
        elif num == 6:
            add_button2 = tk.Button(attribute_window, text="删除该装备",
                                    command=lambda: self.update_callback(category, name, 4, attribute_window))
            add_button2.grid(row=row, column=1, padx=10, pady=5, sticky="w")
        add_button3 = tk.Button(attribute_window, text="添加到敌方已选装备",
                                command=lambda: self.update_callback(category, name, 2))
        add_button3.grid(row=row, column=2, padx=10, pady=5, sticky="w")

    def show_category(self, category):
        # 如果当前有显示的框架，先移除它
        if self.current_frame:
            self.current_frame.pack_forget()

        # 创建对应类别的界面并显示
        if category not in self.frames:
            self.frames[category] = self.create_category_frame(self.root, category,self.show_equipment_attributes)

        self.frames[category].pack(fill="both", expand=True, padx=10, pady=10)
        self.current_frame = self.frames[category]



# 运行应用程序
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
