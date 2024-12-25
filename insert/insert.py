from insert_equipment_information import insert_equipment_information
from insert_passive_description import insert_passive_description
from insert_active_skill_description import insert_active_skill_description
from insert_attribute_bonus_information import insert_attribute_bonus_information
from insert_ability_attack_information import insert_ability_attack_information

insert_equipment_information(host='localhost', user='root', password='jichenyu666.', database='damage_calculation')
insert_passive_description(host='localhost', user='root', password='jichenyu666.', database='damage_calculation')
insert_active_skill_description(host='localhost', user='root', password='jichenyu666.', database='damage_calculation')
insert_attribute_bonus_information(host='localhost', user='root', password='jichenyu666.', database='damage_calculation')
insert_ability_attack_information(host='localhost', user='root', password='jichenyu666.', database='damage_calculation')