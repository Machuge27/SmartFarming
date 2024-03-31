from django.urls import path
from . import views
urlpatterns=[
path('',views.home,name='home'),
path('Login/',views.Login_page,name='Login'),
path('Register/',views.register_page,name='Register'),
path('Chatts/',views.chatts,name='chatts'),
path('Logout/',views.Logout_user,name='Logout'),
path('Farm_data/',views.Farm_data,name='Farm_data'),
path('data_analysis/',views.data_analysis,name='data_analysis'),
path('fetchData/',views.fetchData,name='fetchData'),
path('dm/<int:sender>/<int:receiver>/',views.dm,name='dm'),
path('private/',views.private,name='private'),


]