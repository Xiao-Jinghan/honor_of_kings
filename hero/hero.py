import pymysql
import tkinter as tk
from tkinter import messagebox


class HeroInputForm:
    def __init__(self):
        # 初始化窗口
        self.master = None  # 这里直接创建主窗口
        self.equipment = []
        # 定义所有属性和默认值
        self.attributes = {
            "level" :1,
            "physical_attack": [0, 0],
            "magic_attack": [0, 0],
            "max_health": [0, 0],
            "physical_defense": [0, 0, 0],
            "magic_defense": [0, 0, 0],
            "max_mana": [0, 0],
            "critical_strike": [0, 0],
            "attack_speed": [0, 0],
            "cooldown_reduction": [0, 0],
            "physical_penetration": [0, 0, 0],
            "magic_penetration": [0, 0, 0],
            "movement_speed": [0, 0],
            "physical_lifesteal": [0, 0],
            "magic_lifesteal": [0, 0],
            "hero_type": 'melee',  # 默认值
            "health_per_seconds": [0, 0],
            "mana_per_seconds": [0, 0],
            "tenacity": [0, 0]
        }
        self.critical_strike_effect = 2

    def create_form(self):
        self.master = tk.Tk()  # 这里直接创建主窗口
        self.master.title("Hero Attributes Input Form")
        row = 1  # 从第二行开始，因为第一行显示表头

        # 在最上方显示4列文本：注意,基础值，额外值，百分值
        tk.Label(self.master, text="添加装备后请不要点击clear!").grid(row=0, column=0, padx=10, pady=5)
        tk.Label(self.master, text="基础值").grid(row=0, column=1, padx=10, pady=5)
        tk.Label(self.master, text="额外值").grid(row=0, column=2, padx=10, pady=5)
        tk.Label(self.master, text="百分值").grid(row=0, column=3, padx=10, pady=5)

        for attr_name, attr_value in self.attributes.items():
            label = tk.Label(self.master, text=attr_name)
            label.grid(row=row, column=0, sticky="w", padx=10, pady=5)

            # 如果是 hero_type 字段，使用 OptionMenu 实现选择框
            if attr_name =="level":
                entry = tk.Entry(self.master)
                entry.grid(row=row, column= 1, padx=10, pady=5)
                entry.insert(0, str(self.attributes[attr_name]))  # 显示当前值

                # 更新 self.attributes 当文本变化时
                def update_level(attr_name=attr_name, entry=entry):
                    try:
                        value = entry.get()
                        self.attributes[attr_name] = int(value) if value.isdigit() else 0
                    except ValueError:
                        pass  # 忽略错误输入

                entry.bind("<FocusOut>",
                           lambda event, attr_name=attr_name, entry=entry: update_level(attr_name,entry))
            elif attr_name == "hero_type":
                entry = tk.Entry(self.master)
                entry.grid(row=row, column= 1, padx=10, pady=5)
                entry.insert(0, str(self.attributes[attr_name]))  # 显示当前值

                # 更新 self.attributes 当文本变化时
                def update_type(attr_name=attr_name, entry=entry):
                    try:
                        value = entry.get()
                        self.attributes[attr_name] = value
                    except ValueError:
                        pass  # 忽略错误输入

                entry.bind("<FocusOut>",
                           lambda event, attr_name=attr_name, entry=entry: update_type(attr_name,entry))

            elif len(attr_value) == 3:
                for i in range(len(attr_value)):
                    entry = tk.Entry(self.master)
                    entry.grid(row=row, column=i + 1, padx=10, pady=5)

                    entry.insert(0, str(self.attributes[attr_name][i]))  # 显示当前值
                    # 更新 self.attributes 当文本变化时
                    def update_attribute(attr_name=attr_name, idx=i, entry=entry):
                        try:
                            value = entry.get()
                            if idx == 2:  # 如果是百分比字段，直接保存百分比
                                self.attributes[attr_name][idx] = float(value) if value else 0
                            else:
                                self.attributes[attr_name][idx] = float(value) if value else 0
                        except ValueError:
                            pass  # 忽略错误输入

                    entry.bind("<FocusOut>",
                               lambda event, attr_name=attr_name, idx=i, entry=entry: update_attribute(attr_name, idx,entry))

                    if i == 2:  # 这是第三个输入框，索引从0开始，所以是 i == 2
                        percent_label = tk.Label(self.master, text="%")
                        percent_label.grid(row=row, column=i + 2, padx=10, pady=5)  # 将 % 放在右侧

            # 普通的两个输入框
            elif isinstance(attr_value, list):
                for i in range(len(attr_value)):
                    entry = tk.Entry(self.master)
                    entry.grid(row=row, column=i + 1, padx=10, pady=5)
                    entry.insert(0, str(self.attributes[attr_name][i]))  # 显示当前值

                    # 更新 self.attributes 当文本变化时
                    def update_attribute(attr_name=attr_name, idx=i, entry=entry):
                        try:
                            value = entry.get()
                            self.attributes[attr_name][idx] = float(value) if value else 0
                        except ValueError:
                            pass  # 忽略错误输入

                    entry.bind("<FocusOut>",
                               lambda event, attr_name=attr_name, idx=i, entry=entry: update_attribute(attr_name, idx, entry))

            else:
                entry = tk.Entry(self.master)
                entry.grid(row=row, column=1, padx=10, pady=5)
                entry.insert(0, str(self.attributes[attr_name]))  # 显示当前值

                # 更新 self.attributes 当文本变化时
                def update_attribute(attr_name=attr_name, entry=entry):
                    try:
                        value = entry.get()
                        self.attributes[attr_name] = float(value) if value else 0
                    except ValueError:
                        pass  # 忽略错误输入

                entry.bind("<FocusOut>",
                           lambda event, attr_name=attr_name, entry=entry: update_attribute(attr_name, entry))

            row += 1

        # 提交按钮
        submit_button = tk.Button(self.master, text="Submit", command=self.submit_form)
        submit_button.grid(row=row, column=0, columnspan=3, pady=10)

        # 清空按钮
        clear_button = tk.Button(self.master, text="Clear", command=self.clear_form)
        clear_button.grid(row=row + 1, column=0, columnspan=3, pady=10)

    def submit_form(self):
        # 提交时处理并打印 self.attributes 中的数据
        form_data = {}

        for attr_name, attr_value in self.attributes.items():
            if isinstance(attr_value, list) and len(attr_value) == 3:  # 处理百分比字段
                form_data[attr_name] = [
                    float(attr_value[0]),
                    float(attr_value[1]),
                    float(attr_value[2]) / 100  # 转换为小数
                ]
            elif isinstance(attr_value, list) and len(attr_value) == 2:
                form_data[attr_name] = [float(attr_value[0]), float(attr_value[1])]
            else:
                # 将 "近战" 和 "远程" 转换为 "melee" 和 "ranged"
                self.attributes['hero_type'] = "melee" if attr_value == "近战" else "ranged"

        # 输出输入的内容
        for key, value in form_data.items():
            print(f"{key}: {value}")
        print()
        # 显示提交成功的提示
        messagebox.showinfo("Success", "Form submitted successfully!")

    def clear_form(self):
        # 重置所有属性值为默认值
        for attr_name, default_value in self.attributes.items():
            if isinstance(default_value, list):
                # 重置为默认的数值
                for i in range(len(default_value)):
                    self.attributes[attr_name][i] = 0
            else:
                self.attributes[attr_name] = 0

        # 重新刷新界面
        self.master.destroy()
        self.create_form()

    def base_attribute(self):
        conn = pymysql.connect(
            host="localhost",  # 数据库主机地址
            user="root",  # 数据库用户名
            password="jichenyu666.",  # 数据库密码
            database="damage_calculation"  # 使用的数据库
        )
        cursor = conn.cursor()

        for name in self.equipment:
            # 查询装备详细信息
            query = '''
                SELECT name, price, physical_attack, magic_attack, attack_speed, critical_strike, 
                       physical_lifesteal, cooldown_reduction, max_mana, mana_per_5_seconds, 
                       health_per_5_seconds, max_health, physical_defense, magic_defense, movement_speed
                FROM equipment_information WHERE name = %s
            '''

            cursor.execute(query, (name,))

            equipment = cursor.fetchone()
            for i, value in enumerate(equipment):
                if i == 2 and value != 0:
                    self.attributes['physical_attack'][1] += value
                if i == 3 and value != 0:
                    self.attributes['magic_attack'][1] += value
                if i == 4 and value != 0:
                    self.attributes['attack_speed'][1] += value
                if i == 5 and value != 0:
                    self.attributes['critical_strike'][1] += value
                if i == 6 and value != 0:
                    self.attributes['physical_lifesteal'][1] += value
                if i == 7 and value != 0:
                    self.attributes['cooldown_reduction'][1] += value
                if i == 8 and value != 0:
                    self.attributes['max_mana'][1] += value
                if i == 9 and value != 0:
                    self.attributes['mana_per_seconds'][1] += value / 5
                if i == 10 and value != 0:
                    self.attributes['health_per_seconds'][1] += value / 5
                if i == 11 and value != 0:
                    self.attributes['max_health'][1] += value
                if i == 12 and value != 0:
                    self.attributes['physical_defense'][1] += value
                if i == 13 and value != 0:
                    self.attributes['magic_defense'][1] += value
                if i == 14 and value != 0:
                    self.attributes['movement_speed'][1] += value

        conn.close()

    def attribute(self):
        conn = pymysql.connect(
            host="localhost",  # 数据库主机地址
            user="root",  # 数据库用户名
            password="jichenyu666.",  # 数据库密码
            database="damage_calculation"  # 使用的数据库
        )
        cursor = conn.cursor()
        flag = 1
        hat_flag=0
        while flag != 0:
            flag=0
            for name in self.equipment:
                query = '''
                    SELECT name,passive_skill_name,bonus_attribute,base_bonus_value,bonus_percent_value,bonus_value_or_lower_bound
                            ,bonus_upper_bound,bonus_target_attribute,hero_type
                    FROM attribute_bonus_information WHERE name = %s
                '''
                cursor.execute(query, (name,))
                equipment = cursor.fetchall()
                # 遍历所有的元组
                for idx, record in enumerate(equipment):
                    base1 = 0
                    base2 = 0
                    bonus = 0
                    lower = 0
                    upper = -1
                    result = 0
                    type = 'all'
                    for element_idx, element in enumerate(record):
                        if element_idx == 2 and element != None:
                            if record[3] != None:
                                base1 = record[3]
                            elif record[4] != None:
                                base2 = record[4]
                        if element_idx == 5 and element != None:
                            if element > 1:
                                lower = element
                            else:
                                bonus = element
                        if element_idx == 6 and element != None:
                            upper = element
                        if element_idx == 8 and element != None:
                            type = element
                    if type!='all' and type!=self.attributes['hero_type']:
                        #print(self.attributes['hero_type'],type)
                        pass
                    else:
                        #print(type)
                        if base1!=0 or base2!=0:
                            #print('base')
                            if record[2] =='extra_health':
                                result = base1 + self.attributes['max_health'][1]*base2
                            elif record[0] =='博学者之怒' and hat_flag !=0:
                                #print(self.attributes[record[2]][0],self.attributes[record[2]][1])
                                self.attributes[record[2]][1] = (self.attributes[record[2]][1] +self.attributes[record[2]][0])/1.3 - self.attributes[record[2]][0]
                                #print(self.attributes[record[2]][1],'aaaaa')
                                result = base1 + (self.attributes[record[2]][1] + self.attributes[record[2]][0]) * base2
                                #print(result)
                            else :
                                result = base1 + (self.attributes[record[2]][1]+self.attributes[record[2]][0]) * base2
                                #print(result)
                        elif record[7] =='physical_damage_reduction':
                            result = bonus
                        elif bonus!=0:
                            result = bonus
                        elif lower != 0:
                            result = (upper-lower)/14*(self.attributes['level']-1)+lower
                    print('final',result)
                    if result>upper and upper!=-1:
                        result =upper
                    if (record[7] =='physical_penetration'or record[7] =='magic_penetration') and result<1:
                        self.attributes[record[7]][2] += result*100
                        print(self.attributes[record[7]][2])
                    elif hat_flag !=0:
                        if hat_flag!=result:
                            flag = 1
                        self.attributes[record[7]][1] += result

                    else:
                        if record[0] == '博学者之怒' and hat_flag == 0:
                            hat_flag = result
                            flag = 1
                        if record[0]!= '无尽战刃':
                            self.attributes[record[7]][1] += result
        defense1 = self.attributes['physical_defense'][0]+self.attributes['physical_defense'][1]
        self.attributes['physical_defense'][2] =  defense1 / (defense1+600)
        defense2 = self.attributes['magic_defense'][0]+self.attributes['magic_defense'][1]
        self.attributes['magic_defense'][2] =  defense2 / (defense2+600)
        conn.close()

    def update(self):
        # 获取装备详细信息
        self.base_attribute()
        self.attribute()
        print(self.attributes)

if __name__ == "__main__":
    app = HeroInputForm()  # 创建 HeroInputForm 实例，不需要传递 master
    app.master.mainloop()  # 启动主循环
