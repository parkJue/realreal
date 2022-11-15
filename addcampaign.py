# Campaign 저장
import csv
import os
import django
import re

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "owaste.settings")
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
django.setup()
from zerowaste.models import Campaign

campaign = Campaign()
campaign_list = []

with open('OWASTE - 캠페인.csv', encoding='utf8') as csv_file_campaign:
    rows = csv.reader(csv_file_campaign)
    next(rows, None)
    for row in rows:
        name = row[0]
        start = row[1]
        finish = row[2]
        img = row[3]
        link = row[4]

        campaign = Campaign(name = name,
                            start = start,
                            finish = finish,
                            img = img,
                            link = link)
        campaign_list.append(campaign)

        print(name)
print(len(campaign_list))
Campaign.objects.bulk_create(campaign_list)
Campaign.objects.all().count()