from django.contrib import admin

from .models import Campaign
from .models import Member
from .models import Nkreview
from .models import Oreview
from .models import Shop
from .models import Ask

admin.site.register(Campaign)
admin.site.register(Member)
admin.site.register(Nkreview)
admin.site.register(Oreview)
admin.site.register(Shop)
admin.site.register(Ask)