from django.urls import path
from .views import index,register,registration,register_backend
urlpatterns = [
   path('',index,name='index'),
   path('register1/',register,name='register1'),
   path('register/',registration,name='register'),
   path('register_backend/',register_backend,name='register_backend'),

]