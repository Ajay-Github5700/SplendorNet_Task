from django.urls import path
from .views import *

urlpatterns=[
    path('hv/',hview),
    path('av/',addview),
    path('sv/',showview),
    path('uv/<int:u>/',updateview),
    path('dv/<int:d>/',deleteview),

]