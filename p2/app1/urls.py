from django.urls import path
from .views import index,register,registration,register_backend,log,login_backend,profile,logout_backend
urlpatterns = [
   path('',index,name='index'),
   path('register1/',register,name='register1'),
   path('register/',registration,name='register'),
   path('register_backend/',register_backend,name='register_backend'),
   path('log/', log, name='log'),
   path('login_backend/',login_backend,name='login_backend'),
   path('profile/<str:username>/',profile,name='profile'),
   path('logout_backend/',logout_backend,name='logout_backend'),

]