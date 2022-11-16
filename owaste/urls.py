from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import RedirectView

urlpatterns = [
    # /admin
    path('admin/', admin.site.urls),
    # /owaste
    path('owaste/', include('zerowaste.urls')),
    #common
    path('common/', include('common.urls')),
    #
    path('', RedirectView.as_view(url='/owaste/index'), name="root"),

    re_path(r'^accounts/', include('zerowaste.urls')),
    re_path(r'^accounts/', include('allauth.urls')),
]