from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index),                        # 01. /owaste/index
    path('campaign_list/', views.campaign_list),        # 04. /owaste/campaign_list
    path('shop_search/', views.search, name='search_result'),
    path('shop_info/', views.info, name="info_result"),

    path('detail/<int:id>', views.shop_detail, name="shop_detail"),
    path('detail/<int:shop_pk>/reviews/new/',
         views.review_new, name='review_new'),
    path('detail/<int:shop_pk>/reviews/<int:pk>/edit/',
         views.review_edit, name='review_edit'),
    path('detail/<int:shop_pk>/reviews/<int:pk>/delete/', views.review_delete, name='review_delete')
]