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


# # # Insert into members table
# task = "INSERT INTO members_member (short_name, status, membership, created_by_id, created_on, slug) VALUES (%s, %s, %s, %s, %s, %s)"
# with open('/home/uchechukwu/Documents/projects/ixpn_dashboard/ixpn_dashboard/members.csv') as f:
#     data=[tuple(line) for line in csv.reader(f)]

# new_data = [(data[num][0], data[num][1], data[num][2], data[num][3], date, slugify(data[num][0])) for num in range(len(data))]
# cur.executemany(task, new_data)
# db.commit()

# Insert into ports table
# task = "INSERT INTO members_port (port_capacity, no_of_port, created_by_id, member_id, pop_id, created_on, updated_on, slug, billed) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
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
#                 {{ filter.form.port_capacity|as_crispy_field }}
#               </div>
#               <div class="form-group col-md-4 mb-0">
#                 {{ filter.form.no_of_port|as_crispy_field }}
#               </div>
#           </div>
#         <input type="submit" />
#     </form>
#     {% for obj in filter.qs %}
#     {{ obj.member}} - {{ obj.pop }} - {{ obj.no_of_port }} - {{ obj.port_capacity}}<br />
#     {% endfor %}
#     <br><br><br>

# <div class="form-group col-md-4 mb-0">
#           {{ filter.form.pop|as_crispy_field }}
#         </div>
#         <div class="form-group col-md-4 mb-0">
#             {{ filter.form.port_capacity|as_crispy_field }}
#           </div>
#           <div class="form-group col-md-4 mb-0">
#             {{ filter.form.no_of_port__gt|as_crispy_field }}
#           </div>
#       </div>



a = 99.5
print(round(a))