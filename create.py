from create_active_skill_description_table import create_active_skill_description_table
from create_attribute_bonus_information_table import create_attribute_bonus_information_table
from create_equipment_information_table import create_equipment_information_table
from create_inscription_information_table import create_inscription_information_table
from create_passive_skill_description_table import create_passive_skill_description_table
from create_direct_damage_information_table import create_direct_damage_information_table

create_equipment_information_table(host='localhost', user='root', password='jichenyu666.', database='damage_calculation')
create_passive_skill_description_table(host='localhost', user='root', password='jichenyu666.', database='damage_calculation')
create_active_skill_description_table(host='localhost', user='root', password='jichenyu666.', database='damage_calculation')
create_inscription_information_table(host='localhost', user='root', password='jichenyu666.', database='damage_calculation')
create_attribute_bonus_information_table(host='localhost', user='root', password='jichenyu666.', database='damage_calculation')
create_direct_damage_information_table(host='localhost', user='root', password='jichenyu666.', database='damage_calculation')