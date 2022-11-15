# Nkreview 저장
import csv
import os
import django
import re

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "owaste.settings")
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
django.setup()
from zerowaste.models import Shop, Nkreview

nkreview = Nkreview()
nkreview_list = []

with open('OWASTE - 리뷰.csv', encoding='utf8') as csv_file_nkreview:
    rows = csv.reader(csv_file_nkreview)
    next(rows, None)
    for row in rows:
        shop_id = Shop.objects.get(id=row[0])

        source = row[2]
        nick = row[3]
        reg_date = row[4]
        content = row[5]

        nkreview = Nkreview(shop = shop_id,
                            source=source, 
                            nick=nick, 
                            reg_date=reg_date,
                            content=content)
        nkreview_list.append(nkreview)
        print(nick)
print(len(nkreview_list))
Nkreview.objects.bulk_create(nkreview_list)
Nkreview.objects.all().count()