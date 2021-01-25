from django.contrib import admin
from django.urls import path, re_path

from .views import ShopView, CityView, StreetView


admin.autodiscover()

urlpatterns = [
    path('city/', CityView.as_view()),
    path('shop/', ShopView.as_view({'get':'list', 'post': 'create'})),
    path('city/<int:city_id>/street', StreetView.as_view()),
]
