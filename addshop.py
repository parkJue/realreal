# Shop 저장
import csv
import os
import django
import re

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "owaste.settings")
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
django.setup()
from zerowaste.models import Shop

shop = Shop()
shop_list = []

with open('OWASTE - 매장.csv', encoding='utf8') as csv_file_shop:
    rows = csv.reader(csv_file_shop)
    next(rows, None)
    for row in rows:
        name = row[0]
        category = row[1]
        subject = row[2]
        facility = row[3]
        region = row[4]
        mon = row[5]
        tue = row[6]
        wed = row[7]
        thu = row[8]
        fri = row[9]
        sat = row[10]
        sun = row[11]
        note = row[12]
        page1 = row[13]
        page2 = row[14]
        page3 = row[15]
        tel = row[16]
        tag = row[17]
        address = row[18]
        lat = row[19]
        lon = row[20]
        img = row[21]

        shop = Shop(name = name,
                    category = category,
                    subject = subject,
                    facility = facility,
                    mon = mon,
                    tue = tue,
                    wed = wed,
                    thu = thu,
                    fri = fri,
                    sat = sat,
                    sun = sun,
                    note = note,
                    page1 = page1,
                    page2 = page2,
                    page3 = page3,
                    tel = tel,
                    tag = tag,
                    region = region,
                    address = address,
                    lat = lat,
                    lon = lon,
                    img = img)
        shop_list.append(shop)

        print(name)
print(len(shop_list))
Shop.objects.bulk_create(shop_list)
Shop.objects.all().count()