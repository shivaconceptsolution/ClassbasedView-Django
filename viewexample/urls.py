from django.urls import path
from . import views
from .views import SCSCreate
urlpatterns=[

path('',SCSCreate.as_view()),
path('hello',views.hello,name='hello')

]