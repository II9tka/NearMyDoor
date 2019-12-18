from django.urls import path
from django.urls import include
from .views import *


urlpatterns = [
    path('session/', include('allauth.urls')),
    path('account/<username>/', PageUserView.as_view(), name='username_url'),
]