from app2.views import *

from django.urls import path

app_name='shashi'

urlpatterns=[
    path('fun3/',fun3,name='fun3'),
    path('fun4/',fun4,name='fun4')
]