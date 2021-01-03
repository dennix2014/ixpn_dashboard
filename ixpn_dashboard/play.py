#!/usr/bin/env python3

import psycopg2 as msconn
from django.utils import timezone
import datetime

created_on = timezone.now
updated_on = timezone.now




db = msconn.connect(
	host="localhost",
	user="dennix",
	password="MrMan@1989#",
	database="ixpndash"
	)

cur = db.cursor()



# <select>
#     <option disabled selected>--Select State--</option>
#     <option value="Abia">Abia</option>
#     <option value="Adamawa">Adamawa</option>
#     <option value="Akwa Ibom">Akwa Ibom</option>
#     <option value="Anambra">Anambra</option>
#     <option value="Bauchi">Bauchi</option>
#     <option value="Bayelsa">Bayelsa</option>
#     <option value="Benue">Benue</option>
#     <option value="Borno">Borno</option>
#     <option value="Cross Rive">Cross River</option>
#     <option value="Delta">Delta</option>
#     <option value="Ebonyi">Ebonyi</option>
#     <option value="Edo">Edo</option>
#     <option value="Ekiti">Ekiti</option>
#     <option value="Enugu">Enugu</option>
#     <option value="FCT">Federal Capital Territory</option>
#     <option value="Gombe">Gombe</option>
#     <option value="Imo">Imo</option>
#     <option value="Jigawa">Jigawa</option>
#     <option value="Kaduna">Kaduna</option>
#     <option value="Kano">Kano</option>
#     <option value="Katsina">Katsina</option>
#     <option value="Kebbi">Kebbi</option>
#     <option value="Kogi">Kogi</option>
#     <option value="Kwara">Kwara</option>
#     <option value="Lagos">Lagos</option>
#     <option value="Nasarawa">Nasarawa</option>
#     <option value="Niger">Niger</option>
#     <option value="Ogun">Ogun</option>
#     <option value="Ondo">Ondo</option>
#     <option value="Osun">Osun</option>
#     <option value="Oyo">Oyo</option>
#     <option value="Plateau">Plateau</option>
#     <option value="Rivers">Rivers</option>
#     <option value="Sokoto">Sokoto</option>
#     <option value="Taraba">Taraba</option>
#     <option value="Yobe">Yobe</option>
#     <option value="Zamfara">Zamfara</option>
# </select>



import csv
from django.utils import timezone
from django.utils.text import slugify
#from core.utils import generate_random_string
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

import random
import string

ALPHANUMERIC_STRING = string.ascii_lowercase + string.digits
STRING_LENGTH = 4

def generate_random_string(chars=ALPHANUMERIC_STRING, length=STRING_LENGTH):
    return "".join(random.choice(chars) for _ in range(length))




time = timezone.now()
date = datetime.date.today()
i_d = 1


# # # Insert into members table
# task = "INSERT INTO members_member (short_name, status, membership, created_by_id, created_on, slug) VALUES (%s, %s, %s, %s, %s, %s)"
# with open('/home/uchechukwu/Documents/projects/ixpn_dashboard/ixpn_dashboard/members.csv') as f:
#     data=[tuple(line) for line in csv.reader(f)]

# new_data = [(data[num][0], data[num][1], data[num][2], data[num][3], date, slugify(data[num][0])) for num in range(len(data))]
# cur.executemany(task, new_data)
# db.commit()

# # Insert into members table
task = "INSERT INTO members_switchport (name, switch_id, int_type, media, created_by_id, created_on, slug) VALUES (%s, %s, %s, %s, %s, %s, %s)"
with open('/home/uchechukwu/Documents/projects/ixpn_dashboard/ixpn_dashboard/swiport.csv') as f:
    data=[tuple(line) for line in csv.reader(f)]

new_data = [(data[num][0], data[num][1], data[num][2], data[num][3], i_d, date, slugify(data[num][0] + '-' + data[num][1])) for num in range(len(data))]
cur.executemany(task, new_data)
db.commit()

# Insert into ports table
# task = "INSERT INTO members_port (port_capapot, no_of_port, created_by_id, member_id, pop_id, created_on, updated_on, slug, billed) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
# with open('/home/uchechukwu/Documents/projects/ixpn_dashboard/ixpn_dashboard/ports.csv') as f:
#     data=[tuple(line) for line in csv.reader(f)]

# new_data = [(data[num][0], data[num][1], data[num][2], data[num][3], data[num][4], time, time, (slugify(self.member.name + "-" + self.pop.name) + "-" +generate_random_string())) for num in range(len(data))]
# cur.executemany(task, new_data)
# db.commit()

# num = 10000000
# print(f"{num:,}")

# <hr>
#     <hr>
#     <form method="get">
#         <div class="form-row">
#             <div class="form-group col-md-4 mb-0">
#               {{ filter.form.pop|as_crispy_field }}
#             </div>
#             <div class="form-group col-md-4 mb-0">
#                 {{ filter.form.port_capapot|as_crispy_field }}
#               </div>
#               <div class="form-group col-md-4 mb-0">
#                 {{ filter.form.no_of_port|as_crispy_field }}
#               </div>
#           </div>
#         <input type="submit" />
#     </form>
#     {% for obj in filter.qs %}
#     {{ obj.member}} - {{ obj.pop }} - {{ obj.no_of_port }} - {{ obj.port_capapot}}<br />
#     {% endfor %}
#     <br><br><br>

# <div class="form-group col-md-4 mb-0">
#           {{ filter.form.pop|as_crispy_field }}
#         </div>
#         <div class="form-group col-md-4 mb-0">
#             {{ filter.form.port_capapot|as_crispy_field }}
#           </div>
#           <div class="form-group col-md-4 mb-0">
#             {{ filter.form.no_of_port__gt|as_crispy_field }}
#           </div>
#       </div>



# a = 99.5
# print(round(a))

# a = SwitchPort.objects.filter(switch__pk = 1)
# b = Aka.objects.filter(switch__pk = 1 )


# select 

# select port_id from members_switchport where switch_id = 1 full join members_aka on switch_id = 1 whe



# SELECT pot_id
# FROM
#     members_switchport
#     LEFT JOIN members_aka
#         ON switch_id = 1;

    

# SELECT name
# FROM members_switchport
# WHERE members_switchport.switch_id = 1 and members_switchport.id not in (select members_aka.pot_id from members_aka where members_aka.switch_id = 1)

# b = Aka.objects.filter(switch_id = 1).values('pot_id')
# a = SwitchPort.objects.filter(switch_id=1).exclude(id__in=Aka.objects.filter(switch_id = 1).values('pot_id'))

# if 'switch' in self.data:
#     try:
#         switch_id = int(self.data.get('switch'))
#         self.fields['pot'].queryset = Aka.objects.filter(switch_id=switch_id)
#     except (ValueError, TypeError):
#         pass  # invalid input from the client; ignore and fallback to empty pot queryset
# elif self.instance.pk:
#     self.fields['pot'].queryset = self.instance.switch.pot_set



# Ethernet1
# Ethernet2
# Ethernet3
# Ethernet4
# Ethernet5
# Ethernet6
# Ethernet7
# Ethernet8
# Ethernet9
# Ethernet10
# Ethernet11
# Ethernet12
# Ethernet13
# Ethernet14
# Ethernet15
# Ethernet16
# Ethernet17
# Ethernet18
# Ethernet19
# Ethernet20
# Ethernet21
# Ethernet22
# Ethernet23
# Ethernet24
# Ethernet25
# Ethernet26
# Ethernet27
# Ethernet28
# Ethernet29
# Ethernet30
# Ethernet31
# Ethernet32
# Ethernet33
# Ethernet34
# Ethernet35
# Ethernet36
# Ethernet37
# Ethernet38
# Ethernet39
# Ethernet40
# Ethernet41
# Ethernet42
# Ethernet43
# Ethernet44
# Ethernet45
# Ethernet46
# Ethernet47
# Ethernet48
# Ethernet49
# Ethernet50
# Ethernet51
# Ethernet52
# Ethernet53
# Ethernet54
# Ethernet55
# Ethernet56
# Ethernet57
# Ethernet58
# Ethernet59
# Ethernet60
# Ethernet61
# Ethernet62
# Ethernet63
# Ethernet64
# Ethernet65
# Ethernet66
# Ethernet67
# Ethernet68
# Ethernet69
# Ethernet70
# Ethernet71
# Ethernet72
# Ethernet73
# Ethernet74
# Ethernet75
# Ethernet76
# Ethernet77
# Ethernet78
# Ethernet79
# Ethernet80
# Ethernet81
# Ethernet82
# Ethernet83
# Ethernet84
# Ethernet85
# Ethernet86
# Ethernet87
# Ethernet88
# Ethernet89
# Ethernet90
# Ethernet91
# Ethernet92
# Ethernet93
# Ethernet94
# Ethernet95
# Ethernet96
